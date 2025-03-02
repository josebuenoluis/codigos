import PyPDF2
import re
import time
import json
from openai import OpenAI
import os

# Inicializar el cliente de OpenAI
API_KEY = os.getenv('%OPENAI_API_KEY%')
client = OpenAI(api_key=API_KEY)  # Reemplaza con tu clave API

def extraer_texto_pdf_directo(archivo_pdf):
    """Extrae texto directamente de un objeto UploadedFile"""
    texto_completo = ""
    try:
        lector_pdf = PyPDF2.PdfReader(archivo_pdf)
        for pagina in lector_pdf.pages:
            texto_completo += pagina.extract_text()
    except Exception as e:
        raise Exception(f"Error al leer el PDF: {str(e)}")
    return texto_completo

def dividir_texto_en_secciones(texto, num_secciones=10):
    """
    Divide el texto en secciones aproximadamente iguales.

    Args:
        texto (str): Texto completo extraído del PDF.
        num_secciones (int): Número de secciones a crear.

    Returns:
        list: Lista de secciones de texto.
    """
    # Dividir el texto en oraciones usando expresiones regulares
    oraciones = re.split(r'(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?])$', texto)

    # Filtrar oraciones vacías
    oraciones = [oracion.strip() for oracion in oraciones if oracion.strip()]

    # Calcular el número de oraciones por sección
    oraciones_por_seccion = max(1, len(oraciones) // num_secciones)

    # Crear las secciones
    secciones = []
    for i in range(0, len(oraciones), oraciones_por_seccion):
        seccion = " ".join(oraciones[i:i + oraciones_por_seccion])
        secciones.append(seccion)

    return secciones

def optimizar_texto(texto, max_tokens=800):
    """
    Optimiza el texto para reducir tokens manteniendo la información más relevante.
    Versión modificada que no depende de NLTK sent_tokenize.

    Args:
        texto (str): Texto completo extraído del PDF.
        max_tokens (int): Número máximo aproximado de tokens a mantener.

    Returns:
        str: Texto optimizado.
    """
    # Dividir el texto en oraciones usando expresiones regulares
    oraciones = re.split(r'(?<=[.!?])\s+(?=[A-Z])|(?<=[.!?])$', texto)

    # Filtrar oraciones vacías
    oraciones = [oracion.strip() for oracion in oraciones if oracion.strip()]

    # Eliminar oraciones duplicadas o muy similares
    oraciones_unicas = []
    for oracion in oraciones:
        # Normalizar la oración (eliminar espacios extra, convertir a minúsculas)
        oracion_norm = re.sub(r'\s+', ' ', oracion).strip().lower()

        # Verificar si una oración similar ya está en la lista
        es_duplicada = False
        for oracion_existente in oraciones_unicas:
            oracion_existente_norm = re.sub(r'\s+', ' ', oracion_existente).strip().lower()
            # Si hay más de 80% de similitud, considerar como duplicada
            if len(oracion_norm) > 0 and len(oracion_existente_norm) > 0:
                # Calcular similitud basada en caracteres comunes
                chars_comunes = sum(1 for c in oracion_norm if c in oracion_existente_norm)
                similitud = chars_comunes / max(len(oracion_norm), len(oracion_existente_norm))
                if similitud > 0.8:
                    es_duplicada = True
                    break

        if not es_duplicada and len(oracion.strip()) > 0:
            oraciones_unicas.append(oracion)

    # Estimar tokens (aproximadamente 1.3 tokens por palabra)
    palabras_por_oracion = [len(oracion.split()) for oracion in oraciones_unicas]
    tokens_estimados = [int(palabras * 1.3) for palabras in palabras_por_oracion]

    # Seleccionar oraciones hasta alcanzar el límite de tokens
    texto_optimizado = ""
    tokens_acumulados = 0

    # Priorizar las primeras oraciones (introducción) y las últimas (conclusiones)
    num_oraciones = len(oraciones_unicas)
    indices_prioritarios = list(range(min(5, num_oraciones))) + list(range(max(0, num_oraciones-5), num_oraciones))
    indices_restantes = list(range(5, max(5, num_oraciones-5)))

    # Ordenar los índices para procesar primero los prioritarios
    indices_ordenados = indices_prioritarios + indices_restantes

    for idx in indices_ordenados:
        if idx < len(oraciones_unicas):
            if tokens_acumulados + tokens_estimados[idx] <= max_tokens:
                texto_optimizado += oraciones_unicas[idx] + " "
                tokens_acumulados += tokens_estimados[idx]
            else:
                # Si ya no caben más oraciones completas, parar
                break

    return texto_optimizado.strip()

def contar_tokens_aproximados(texto):
    """
    Estima el número de tokens en un texto.

    Args:
        texto (str): Texto a analizar.

    Returns:
        int: Número estimado de tokens.
    """
    # Aproximación: 1 token ≈ 4 caracteres en inglés o 1.3 tokens por palabra
    palabras = len(texto.split())
    return int(palabras * 1.3)

def extraer_tema_principal(texto, max_palabras=5):
    """
    Extrae el tema principal del texto para usar en la corrección de preguntas ambiguas.
    
    Args:
        texto (str): Texto de la sección.
        max_palabras (int): Número máximo de palabras para el tema.
        
    Returns:
        str: Tema principal extraído.
    """
    # Simplificación: usar las primeras palabras del texto como tema
    palabras = texto.split()
    if len(palabras) <= max_palabras:
        return texto
    
    # Tomar las primeras palabras significativas
    palabras_significativas = []
    for palabra in palabras:
        if len(palabra) > 3 and palabra.lower() not in ['este', 'esta', 'estos', 'estas', 'esos', 'esas', 'aquel', 'aquella']:
            palabras_significativas.append(palabra)
            if len(palabras_significativas) >= max_palabras:
                break
    
    return " ".join(palabras_significativas) if palabras_significativas else "el tema del documento"

def corregir_pregunta_ambigua(pregunta, texto):
    """
    Intenta corregir una pregunta ambigua reemplazando referencias genéricas con el tema específico.
    
    Args:
        pregunta (dict): Pregunta en formato JSON.
        texto (str): Texto de contexto.
        
    Returns:
        dict: Pregunta corregida o None si no se pudo corregir.
    """
    try:
        # Extraer el tema principal del contexto
        tema = extraer_tema_principal(texto)
        
        # Reemplazar referencias ambiguas con el tema específico
        texto_pregunta = pregunta["pregunta"]
        referencias_ambiguas = {
            "este tipo": f"el tipo de {tema}",
            "esta ayuda": f"la ayuda sobre {tema}",
            "este texto": f"el texto sobre {tema}",
            "este documento": f"el documento sobre {tema}",
            "esta sección": f"la sección sobre {tema}"
        }
        
        for ref, reemplazo in referencias_ambiguas.items():
            if ref in texto_pregunta.lower():
                texto_pregunta = re.sub(re.escape(ref), reemplazo, texto_pregunta, flags=re.IGNORECASE)
        
        # Actualizar la pregunta corregida
        pregunta_corregida = pregunta.copy()
        pregunta_corregida["pregunta"] = texto_pregunta
        return pregunta_corregida
    except:
        return None

def generar_cuestionario_json_por_seccion(texto, num_preguntas=8, max_tokens_salida=800):
    """
    Genera un cuestionario en formato JSON basado en una sección de texto usando GPT-3.5-Turbo.
    Versión mejorada para generar preguntas más contextualizadas y específicas.

    Args:
        texto (str): Texto optimizado de la sección.
        num_preguntas (int): Número de preguntas a generar.
        max_tokens_salida (int): Número máximo de tokens para la respuesta.

    Returns:
        list: Lista de preguntas en formato JSON.
    """
    try:
        # Crear el prompt para la API con instrucciones más específicas
        prompt = f"""
        Genera un cuestionario educativo con {num_preguntas} preguntas basadas en el siguiente texto.

        INSTRUCCIONES IMPORTANTES:
        1. Cada pregunta debe ser clara, específica y autocontenida (no debe hacer referencia a "este texto", "esta ayuda", etc. sin contexto).
        2. Evita preguntas ambiguas o que requieran información no presente en el texto.
        3. Las preguntas deben ser relevantes para el contenido del texto y evaluar la comprensión del mismo.
        4. Cada pregunta debe tener 4 opciones de respuesta con una sola respuesta correcta.
        5. Las opciones incorrectas deben ser plausibles pero claramente incorrectas según el texto.

        Devuelve el resultado en formato JSON con la siguiente estructura:
        [
            {{
                "pregunta": "Texto de la pregunta completa y específica",
                "opciones": ["Opción A", "Opción B", "Opción C", "Opción D"],
                "respuesta_correcta": 0  // Índice (0-3) de la opción correcta en el array
            }},
            // Más preguntas...
        ]

        Asegúrate de que el JSON sea válido y que cada pregunta tenga exactamente 4 opciones.

        Texto: {texto}
        """

        # Realizar la consulta a la API usando la nueva sintaxis
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en educación especializado en crear cuestionarios de alta calidad. Tus preguntas deben ser claras, específicas, contextualizadas y evaluar correctamente la comprensión del material."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens_salida,
            temperature=0.7
        )

        # Extraer y devolver el cuestionario generado
        cuestionario_json_texto = response.choices[0].message.content

        # Extraer solo el JSON de la respuesta (eliminar texto adicional si existe)
        json_match = re.search(r'\[.*\]', cuestionario_json_texto, re.DOTALL)
        if json_match:
            cuestionario_json_texto = json_match.group(0)

        # Convertir el texto JSON a una lista de Python
        cuestionario_json = json.loads(cuestionario_json_texto)

        # Verificar y mejorar la calidad de las preguntas
        cuestionario_mejorado = []
        preguntas_omitidas = 0
        
        for pregunta in cuestionario_json:
            # Verificar si la pregunta contiene referencias ambiguas
            texto_pregunta = pregunta["pregunta"]
            referencias_ambiguas = ["este tipo", "esta ayuda", "este texto", "este documento", "esta sección"]

            contiene_ambiguedad = any(ref in texto_pregunta.lower() for ref in referencias_ambiguas)

            if not contiene_ambiguedad:
                cuestionario_mejorado.append(pregunta)
            else:
                # Intentar corregir la pregunta ambigua
                pregunta_corregida = corregir_pregunta_ambigua(pregunta, texto)
                if pregunta_corregida:
                    cuestionario_mejorado.append(pregunta_corregida)
                    print(f"Pregunta corregida: {pregunta_corregida['pregunta']}")
                else:
                    preguntas_omitidas += 1
                    print(f"Omitiendo pregunta ambigua: {texto_pregunta}")

        # Calcular tokens utilizados
        tokens_entrada = contar_tokens_aproximados(prompt)
        tokens_salida = contar_tokens_aproximados(cuestionario_json_texto)

        print(f"Tokens de entrada: ~{tokens_entrada}")
        print(f"Tokens de salida: ~{tokens_salida}")
        print(f"Costo estimado: ${(tokens_entrada/1000*0.0015) + (tokens_salida/1000*0.002):.6f}")
        print(f"Preguntas generadas: {len(cuestionario_mejorado)} (se omitieron {preguntas_omitidas} preguntas ambiguas)")

        return cuestionario_mejorado

    except Exception as e:
        print(f"Error al generar el cuestionario JSON: {str(e)}")
        if 'response' in locals():
            print(f"Respuesta recibida: {response.choices[0].message.content}")
        return []

def guardar_cuestionario_json(cuestionario_json, nombre_archivo):
    """
    Guarda el cuestionario generado en un archivo JSON.

    Args:
        cuestionario_json (list): Lista de preguntas en formato JSON.
        nombre_archivo (str): Nombre del archivo de salida.
    """
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(cuestionario_json, archivo, ensure_ascii=False, indent=2)
        print(f"Cuestionario JSON guardado en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el cuestionario JSON: {str(e)}")

def procesar_pdf_y_generar_cuestionario_json(texto_completo, total_preguntas=60, max_tokens_entrada=800, max_tokens_salida=800):
    """
    Procesa un PDF grande y genera un cuestionario en formato JSON con muchas preguntas,
    dividiendo el proceso en secciones para optimizar costos.
    Versión mejorada para asegurar que se generen todas las preguntas solicitadas.

    Args:
        ruta_pdf (str): Ruta al archivo PDF.
        total_preguntas (int): Número total de preguntas a generar.
        max_tokens_entrada (int): Número máximo de tokens para el texto de entrada por sección.
        max_tokens_salida (int): Número máximo de tokens para la respuesta por sección.

    Returns:
        list: Lista completa de preguntas en formato JSON.
    """
    # Extraer texto del PDF
    # print(f"Extrayendo texto de {ruta_pdf}...")
    # texto_completo = extraer_texto_pdf(ruta_pdf)

    if not texto_completo:
        return []

    # Calcular el número de secciones necesarias
    preguntas_por_seccion = 8  # Aumentado de 6 a 8 preguntas por sección
    num_secciones = (total_preguntas + preguntas_por_seccion - 1) // preguntas_por_seccion

    # Dividir el texto en secciones
    print(f"Dividiendo el texto en {num_secciones} secciones...")
    secciones = dividir_texto_en_secciones(texto_completo, num_secciones)

    # Lista para almacenar todas las preguntas
    todas_las_preguntas = []
    costo_total = 0
    preguntas_generadas = 0

    # Procesar cada sección
    i = 0
    while preguntas_generadas < total_preguntas and i < len(secciones):
        seccion = secciones[i]
        print(f"\nProcesando sección {i+1}/{len(secciones)}...")

        # Optimizar el texto de la sección
        texto_optimizado = optimizar_texto(seccion, max_tokens_entrada)

        # Calcular cuántas preguntas generar en esta sección
        preguntas_restantes = total_preguntas - preguntas_generadas
        preguntas_a_generar = min(preguntas_por_seccion, preguntas_restantes)

        # Generar cuestionario para esta sección
        print(f"Generando {preguntas_a_generar} preguntas para la sección {i+1}...")
        preguntas_seccion = generar_cuestionario_json_por_seccion(
            texto_optimizado,
            num_preguntas=preguntas_a_generar,
            max_tokens_salida=max_tokens_salida
        )

        # Si generamos menos preguntas de las esperadas, intentar de nuevo con parámetros diferentes
        if len(preguntas_seccion) < preguntas_a_generar:
            preguntas_faltantes = preguntas_a_generar - len(preguntas_seccion)
            print(f"Se generaron solo {len(preguntas_seccion)} de {preguntas_a_generar} preguntas. Generando {preguntas_faltantes} preguntas adicionales...")
            
            # Intentar con un prompt ligeramente diferente o más tokens
            preguntas_adicionales = generar_cuestionario_json_por_seccion(
                texto_optimizado,
                num_preguntas=preguntas_faltantes,
                max_tokens_salida=max_tokens_salida + 200  # Aumentar tokens para el reintento
            )
            
            preguntas_seccion.extend(preguntas_adicionales)
            print(f"Total de preguntas generadas para esta sección después del reintento: {len(preguntas_seccion)}")

        # Agregar las preguntas a la lista completa
        todas_las_preguntas.extend(preguntas_seccion)

        # Actualizar contador de preguntas
        preguntas_generadas += len(preguntas_seccion)

        # Calcular costo de esta sección
        tokens_entrada = contar_tokens_aproximados(texto_optimizado)
        tokens_salida = contar_tokens_aproximados(json.dumps(preguntas_seccion))
        costo_seccion = (tokens_entrada/1000*0.0015) + (tokens_salida/1000*0.002)
        costo_total += costo_seccion

        print(f"Costo de la sección {i+1}: ${costo_seccion:.6f}")
        print(f"Preguntas generadas hasta ahora: {preguntas_generadas}/{total_preguntas}")

        # Incrementar el contador de secciones
        i += 1

        # Si hemos procesado todas las secciones pero aún necesitamos más preguntas,
        # volvemos a procesar algunas secciones con diferentes parámetros
        if i >= len(secciones) and preguntas_generadas < total_preguntas:
            print("\nNo se generaron suficientes preguntas. Procesando secciones adicionales...")
            # Reiniciar el contador para procesar secciones adicionales
            i = 0
            # Aumentar el número de preguntas por sección para las iteraciones adicionales
            preguntas_por_seccion += 2

        # Pequeña pausa para evitar límites de rate en la API
        time.sleep(1)

    print(f"\nCosto total del cuestionario: ${costo_total:.6f}")
    print(f"Costo promedio por pregunta: ${costo_total/preguntas_generadas:.6f}")
    

    return todas_las_preguntas

# Ejemplo de uso
# if __name__ == "__main__":
#     # Ruta al archivo PDF
#     ruta_pdf = "UT6-Teoría.pdf"  # Reemplaza con la ruta a tu PDF

#     # Procesar el PDF y generar el cuestionario en formato JSON
#     cuestionario_json = procesar_pdf_y_generar_cuestionario_json(
#         ruta_pdf,
#         total_preguntas=60,  # Número total de preguntas a generar
#         max_tokens_entrada=800,  # Límite de tokens para el texto de entrada por sección
#         max_tokens_salida=800  # Límite de tokens para la respuesta por sección (aumentado)
#     )

#     print("\nCuestionario en formato JSON generado y guardado con éxito!")
#     print(f"Total de preguntas generadas: {len(cuestionario_json)}")