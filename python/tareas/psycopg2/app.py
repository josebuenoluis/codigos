from conexion import conexion
from tablas import crear_tablas
from datetime import datetime
import re
import psycopg2

# Se debe crear un sistema para gestionar la información de una tienda de 
# música. Este sistema permitirá registrar discos, artistas, géneros musicales y 
# las ventas realizadas. Cada disco puede involucrar varios artistas y estar 
# clasificado en múltiples géneros. Además, las ventas deben incluir información 
# sobre los clientes y los discos vendidos.

# a) Create: Insertar nuevos discos, artistas y ventas. 
# b) Read: Consultar información de discos, artistas y ventas. 
# c) Update: Actualizar información de discos y ventas. 
# d) Delete: Eliminar discos, artistas o ventas de la base de datos. 

# a) ¿Qué discos incluyen un género musical específico? 
# b) ¿Qué discos ha comprado un cliente determinado? 
# c) ¿Cuáles son los artistas que han colaborado en un disco específico? 

#==================== UTILS =========================

def validar_fecha(fecha:str):
    try:
        fecha_valida = datetime.strptime(fecha,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def mostrar_discos() -> tuple[list[str],str]:
    """Funcion para obtener los nombres de los discos
    existentes y devolver una cadena para mostrarlos."""
    cursor = db.cursor()
    consulta = "SELECT * FROM discos;"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    cadena = []
    discos_existentes = []
    if len(resultado) > 0:
        for disco in resultado:
            datos_disco = f"""
    Titulo:                {disco[1]}
    Año de lanzamiento:    {disco[2]}
    Generos musicales:     {disco[3]}
    Artistas involucrados: {disco[4]}
"""
            discos_existentes.append(disco[1])
            cadena.append(datos_disco)
        cadena = "\n".join(cadena)
    return discos_existentes,cadena


def obtener_discos() -> list[str]:
    """Funcion para pedir discos vendidos al usuario
    mediante un bucle."""
    discos_vendidos = []
    discos_existentes,mostrar = mostrar_discos()
    while True:
        print(mostrar)
        disco = input("\nIngrese el nombre del disco o presione ENTER para salir: ")
        if disco in discos_existentes:
            discos_vendidos.append(disco)
        elif disco == "":
            print("\nSaliendo del bucle...")
            break
        else:
            print("\nEl disco ingresado no existe, vuelva a intentar.")
    return discos_vendidos

def obtener_generos() -> list[str]:
    """Funcion para obtener generos musicales mediante
    un bucle."""
    generos_musicales = []
    while True:
        print(f"\nGeneros añadidos: {generos_musicales}")
        genero = input("\nIngrese genero musical o ENTER para salir: ")
        if genero != "":
            generos_musicales.append(genero)
        else:
            print("\nSaliendo del bucle...")
            break
    return generos_musicales

def mostrar_artistas() -> tuple[list[int],str]:
    """Funcion para obtener una lista de ID de 
    artistas y mostrar los artista con su ID."""
    cursor = db.cursor()
    consulta = "SELECT * FROM artistas;"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    id_artistas = []
    cadena = []
    if len(resultado) > 0:
        for artista in resultado:
            datos_artista = artista[1].strip("()").split(",")
            artista_string = f"""    
    ID:           {artista[0]}
    Nombre:       {datos_artista[0]}
    Apellido:     {datos_artista[1]}
    Nacionalidad: {datos_artista[2]}"""
            cadena.append(artista_string)
            id_artistas.append(artista[0])
        cadena = "\n".join(cadena)
    cursor.close()
    return (id_artistas,cadena)

def obtener_artistas() -> list[int]:
    """Funcion para obtener los artistas involucrados
    mediante un bucle mostrando los artistas existentes con su ID."""
    artistas_involucrados = []
    while True:
        id_artistas,mostrar = mostrar_artistas()
        print(f"\nArtistas existentes: {mostrar}")
        print(f"\nArtistas seleccionados: {artistas_involucrados}")
        artista_id = input("\nIngrese ID del artista o presione ENTER para salir: ")
        if artista_id.isdigit():
            artista_id = int(artista_id)
            if artista_id in id_artistas:
                artistas_involucrados.append(artista_id)
            else:
                print("\nEl artista ingresado no existe.")
        elif artista_id == "":
            print("\nSaliendo del bucle...")
            break
        else:
            print("\nDebe ingresar un ID valido disponible.")
        
    return artistas_involucrados

def mostrar_ventas() -> tuple[list[int],str]:
    """Funcion para obtener una lista de ID de 
    ventas y mostrar las ventas con su ID."""
    cursor = db.cursor()
    consulta = "SELECT * FROM ventas;"
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    id_ventas = []
    cadena = []
    if len(resultado) > 0:
        for venta in resultado:
            nombre_cliente = re.findall(r'([A-Z|a-z]+)\,',venta[1])[0]
            fecha_venta = re.findall(r'\d+[-]\d+[-]\d+',venta[1])[0]
            array_string = """SELECT array_to_string(((datos_venta).discos_vendidos).articulos_comprados,', ') AS discos_comprados
            FROM ventas
            WHERE id = %s;"""
            cursor_array = db.cursor()
            cursor_array.execute(array_string,(venta[0],))
            discos_comprados = cursor_array.fetchone()
            discos_comprados = ", ".join(discos_comprados)
            venta_string = f"""    
    ID:               {venta[0]}
    Nombre cliente:   {nombre_cliente}
    Fecha de venta:   {fecha_venta}
    Discos comprados: {discos_comprados}"""
            cadena.append(venta_string)
            id_ventas.append(venta[0])
        cadena = "\n".join(cadena)
    cursor.close()
    return (id_ventas,cadena)
# =====================================================

# =================== INSERCIONES =====================

def insertar_artista() -> bool:
    """Funcion para insertar un nuevo artista con
    un tipo de dato compuesto artist_type"""
    cursor = db.cursor()
    nombre = input("\nIngrese nombre del artista: ").strip()
    apellido = input("\nIngrese apellido del artista: ").strip()
    nacionalidad = input("\nIngrese nacionalidad: ").strip()
    artista = (nombre,apellido,nacionalidad)
    if nombre.isalpha() and apellido.isalpha() and nacionalidad.isalpha():
        command = """INSERT INTO artistas(datos)
        VALUES ((%s,%s,%s)::artist_type);"""
        cursor.execute(command,artista)
        db.commit()
        cursor.close()
        print("\nArtista insertado correctamente.")
    elif nombre == "" and apellido == "" and nacionalidad == "":
        print("\nERROR: Los campos no pueden estar vacios.")
    else:
        print("\nERROR: Los campos deben ser valores alfabeticos.")

def insertar_disco() -> None:
    """Funcion para insertar un nuevo disco con arrays que
    contendran datos para relacionar estos discos con otros datos"""
    command = """INSERT INTO public.discos(
	titulo, "año_lanzamiento", generos_musicales, artistas_involucrados)
	VALUES (%s,%s,%s,%s);"""
    titulo = input("\nIngrese el titulo: ")
    anio_lanzamiento = input("\nIngrese el año de lanzamiento: ")
    generos_musicales = obtener_generos()
    artistas_involucrados = obtener_artistas()
    if titulo != "" and anio_lanzamiento != "" and anio_lanzamiento.isdigit() and \
    len(generos_musicales) > 0 and len(artistas_involucrados) > 0:
        cursor = db.cursor()
        cursor.execute(command,(titulo,anio_lanzamiento,generos_musicales,artistas_involucrados))
        db.commit()
        cursor.close()
        print("\nDisco insertado correctamente...")
    elif len(generos_musicales) == 0 and len(artistas_involucrados) == 0:
        print("\nERROR: Las listas de generos musicales o artistas involucrados, no pueden estar vacias.")
    else:
        print("\nERROR: Los datos ingresados no son validos.")

def registrar_venta() -> bool:
    """Funcion para registrar una venta con tipos de 
    datos compuestos y un array para almacenar los id de discos"""
    
    
    command = """INSERT INTO public.ventas(
	datos_venta)
	VALUES(ROW(%s,ROW(%s)::sale_date,ROW(%s)::items_purchased)::sale_info);"""

    cliente = input("\nIngrese el nombre del cliente: ")
    fecha_venta = input("\nIngrese fecha de la venta: ")
    discos_vendidos = obtener_discos()
    if cliente.isalpha() and validar_fecha(fecha_venta) and len(discos_vendidos) > 0:
        cursor = db.cursor()
        cursor.execute(command,(cliente,fecha_venta,discos_vendidos))
        db.commit()
        print("\nVenta registrada correctamente...")
    else:
        print("\nLos datos ingresados no son validos...")

# ====================== CONSULTAS ==========================

def consulta_genero_especifico() -> None:
    """Funcion para consultar los discos que
    incluyen un genero musical especifico."""
    cursor = db.cursor()
    consulta_generos = "SELECT distinct(unnest(generos_musicales)) FROM discos;"
    cursor.execute(consulta_generos)
    resultado = cursor.fetchall()
    if len(resultado) > 0:
        generos = [genero[0] for genero in resultado]
        print(" ")
        print("\n".join([f"{genero+1}. {generos[genero]}" for genero in range(len(generos))]))
        print(" ")
        cursor.close()
        user = input("\nIngrese el genero para consultar los discos: ")
        if user.isdigit():
            user = int(user)
            if user <= len(generos) and user > 0:
                genero = generos[user-1]
                consulta = """
                SELECT *
                FROM discos
                WHERE array_position(generos_musicales,%s) > 0;"""
                cursor = db.cursor()
                cursor.execute(consulta,(genero,))
                resultado = cursor.fetchall()
                print(f"\nDiscos dentro del genero '{genero}':")
                for disco in resultado:
                    cadena = f"""
                Titulo: {disco[1]}
                Año de estreno: {disco[2]}
                Generos musicales: {disco[3]}"""
                    print(cadena)
            else:
                print("\nEl valor ingresado no corresponde con ningun genero de la lista.")
        else:
            print("\nDebe ingresar un valor numerico.")
    else:
        print("\nNo se encuentran generos...")

def consulta_cliente_determinado() -> None:
    """Funcion para consultar los discos que 
    ha comprado un cliente determinado."""
    consulta_clientes = "SELECT (datos_venta).customer_name FROM ventas;"
    cursor = db.cursor()
    cursor.execute(consulta_clientes)
    resultado_clientes = cursor.fetchall()
    if len(resultado_clientes) > 0:
        print("\nCliente: ")
        clientes = [cliente[0] for cliente in resultado_clientes]
        print(" ")
        print("\n".join([f"- {clientes[cliente]}" for cliente in range(len(clientes))]))
        print(" ")
        user = input("\nIngrese el nombre del cliente: ")
        if user != "" and user in clientes:
            consulta = """SELECT array_to_string(((datos_venta).discos_vendidos).articulos_comprados,',')
            FROM ventas
            where (datos_venta).customer_name LIKE %s;"""
            cursor = db.cursor()
            cursor.execute(consulta,(user,))
            resultado = cursor.fetchall()
            print(f"\nDiscos comprados por el cliente '{user}': \n")
            for disco in resultado[0][0].split(","):
                print(f"- Titulo: {disco}")
        else:
            print("\nEl cliente ingresado no se encuentra...")
    else:
        print("\nNo se encuentran clientes.")
def consulta_artistas_disco_colaborado() -> None:
    """Funcion para consultar los artistas que
    han colaborado en un disco especifico."""
    titulo_disco,mostrar = mostrar_discos()
    print(mostrar)
    user = input("\nIngrese el titulo del disco: ")
    if user != "":
        if user in titulo_disco:
            consulta = """
            SELECT (datos).nombre,(datos).apellido
            FROM discos,artistas
            WHERE titulo LIKE %s AND artistas.id = ANY(artistas_involucrados);"""
            cursor = db.cursor()
            cursor.execute(consulta,(user,))
            resultado = cursor.fetchall()
            print("\nArtistas: ")
            for artista in resultado:
                print(f"- Nombre Artista: {artista[0]} {artista[1]}")
        else:
            print("\nEl titulo ingresado no se encuentra...")
    else:
        print("\nEl campo no puede estar vacio.")

# =========================================================

#===================== DELETE ===============================

def eliminar_artista() -> None:
    """Funcion para eliminar un artista por su id."""
    command = """DELETE FROM public.artistas
	WHERE id = %s;"""
    while True:
        id_artistas,mostrar = mostrar_artistas()
        print(mostrar)
        artista = input("\nIngrese el ID del artista o presione ENTER para cancelar: ")
        if artista.isdigit():
            if int(artista) in id_artistas:
                cursor = db.cursor()
                cursor.execute(command,(artista,))
                db.commit()
                cursor.close()
                print("\nArtista eliminado correctamente...")
            else:
                print("\nEl artista ingresado no existe...")
        elif artista == "":
            print("\nSaliendo a menu principal...")
            break
        else:
            print("\nDebe ingresar un numero entero.")

def eliminar_disco() -> None:
    """Funcion para eliminar un disco por su titulo."""
    command = """DELETE FROM public.discos
	WHERE titulo = %s;"""
    while True:
        titulo_discos,mostrar = mostrar_discos()
        print(mostrar)
        titulo = input("\nIngrese el titulo del disco o presione ENTER para cancelar: ")
        if titulo != "":
            if titulo in titulo_discos:
                cursor = db.cursor()
                cursor.execute(command,(titulo,))
                db.commit()
                cursor.close()
                print("\nDisco eliminado correctamente...")
            else:
                print("\nEl disco ingresado no existe...")
        else:
            print("\nSaliendo a menu principal...")
            break

def eliminar_venta() -> None:
    """Funcion para eliminar una venta por su ID."""
    command = """DELETE FROM public.ventas
	WHERE id = %s;"""
    while True:
        id_ventas,mostrar = mostrar_ventas()
        print(mostrar)
        id = input("\nIngrese el ID de venta o presione ENTER para cancelar: ")
        if id.isdigit():
            id = int(id)
            if id in id_ventas:
                cursor = db.cursor()
                cursor.execute(command,(id,))
                db.commit()
                cursor.close()
                print("\nVenta eliminada correctamente...")
            else:
                print("\nEl ID de venta ingresado no existe...")
        elif id == "":
            print("\nSaliendo a menu principal.")
            break
        else:
            print("\nEl ID ingresado debe ser un numero entero.")


# ==================================================

# =================== UPDATE =======================

def actualizar_disco() -> None:
    """Funcion para actualizar informacion
    de un disco por su titulo."""
    campos = ["Titulo","año_lanzamiento","generos_musicales","artistas_involucrados"]
    posicion_campos = ["1","2","3","4"]
    while True:
        titulo_discos,mostrar = mostrar_discos()
        print(mostrar)
        print("  ".join([f"{campo+1}. {campos[campo]}" for campo in range(len(campos))]))
        campo = input("\nIngrese el campo que desea actualizar o presione ENTER para cancelar: ")
        if campo in posicion_campos:
            campo_string = campos[posicion_campos.index(campo)]
            user = input("\nIngrese el titulo del disco a actualizar o ENTER para salir: ")
            if user in titulo_discos:
                if campo == "1" or campo == "2":
                    nuevo_valor = nuevo_valor = input("\nIngrese el nuevo valor: ")
                    if nuevo_valor != "" and campo_string == "Titulo" or \
                        nuevo_valor.isdigit() and campo_string == "año_lanzamiento":
                        command = f"""
                        UPDATE discos
                        SET {campo_string} = '{nuevo_valor}'
                        WHERE titulo LIKE '{user}';
                        """
                    elif nuevo_valor == "":
                        print("\nEl nuevo valor no puede estar vacio.")
                        continue
                    else:
                        print("\nEl nuevo valor es valido.")
                        continue
                else:
                    print(f"\n1. Añadir un elemento a '{campo_string}'    2. Eliminar un elemento de '{campo_string}'")
                    accion = input(f"Que desea hacer?[1][2]: ")
                    if accion == "1" or accion == "2":
                        valor_array = input(f"\nIngrese el valor a {"añadir" if accion == "1" else "eliminar"}: ")
                        instruccion = "array_append" if accion == "1" else "array_remove"
                        if valor_array != "":
                            command = f"""UPDATE discos
                            SET {campo_string} = {instruccion}({campo_string},'{valor_array}')
                            WHERE titulo LIKE '{user}';"""
                        else:
                            print("\nEl valor no puede estar vacio.")
                            continue
                    else:
                        print("\nNo ha ingresado una accion valida, vuelva a intentar...")
                        continue
                cursor = db.cursor()
                cursor.execute(command)
                db.commit()
                cursor.close()
                print(f"\n'{campo_string}' actualizado correctamente.")
            else:
                print("\nEl 'Titulo' ingresado no se encuentra. ")
        elif campo == "":
            print("\nSaliendo a menu principal...")
            break
        else:
            print("\nDebe ingresar un campo valido.")

def actualizar_venta() -> None:
    """Funcion para actualizar de una
    venta por su ID."""
    campos = ["customer_name","fecha_venta","discos_vendidos"]
    posicion_campos = ["1","2","3"]
    while True:
        id_ventas,mostrar = mostrar_ventas()
        print(mostrar)
        print(" ")
        print("  ".join([f"{campo+1}. {campos[campo]}" for campo in range(len(campos))]))
        campo = input("\nIngrese el campo que desea actualizar o presione ENTER para cancelar: ")
        if campo in posicion_campos:
            campo_string = campos[posicion_campos.index(campo)]
            user = input("\nIngrese el ID de la venta o ENTER para salir: ")
            if user.isdigit():
                user = int(user)
                if user in id_ventas:
                    if campo == "1" or campo == "2":
                        nuevo_valor = input(f"\nIngrese el nuevo valor para '{campo_string}': ")
                        if nuevo_valor != "" and campo_string == "customer_name" or \
                            nuevo_valor != "" and campo_string == "fecha_venta" and validar_fecha(nuevo_valor):
                            command = f"""UPDATE ventas
                            SET datos_venta.{campo_string} = '{nuevo_valor}'
                            WHERE id = {user};"""
                        elif nuevo_valor == "":
                            print("\nEl nuevo valor no puede estar vacio, vuelva a intentar.")
                            continue
                        else:
                            print("\nLos datos ingresados no son validos.")
                            continue
                    elif campo == "3":
                        print(f"\n1. Añadir un elemento a '{campo_string}'    2. Eliminar un elemento de '{campo_string}'")
                        accion = input(f"Que desea hacer?[1][2]: ")
                        if accion == "1" or accion == "2":
                            valor_array = input(f"\nIngrese el valor a {"añadir" if accion == "1" else "eliminar"}: ")
                            instruccion = "array_append" if accion == "1" else "array_remove"
                            if valor_array != "":
                                if instruccion == "array_remove":
                                    command = f"""UPDATE ventas
                                    SET datos_venta = (
                                    (datos_venta).customer_name,               
                                    (datos_venta).fecha_venta,                            
                                    ROW(array_remove(((datos_venta).discos_vendidos).articulos_comprados, '{valor_array}'))::items_purchased
                                    )::sale_info
                                    WHERE id = {user} AND array_position((datos_venta).discos_vendidos.articulos_comprados,'{valor_array}') > 0;
                                    """
                                else:
                                    command = f"""UPDATE ventas
                                    SET datos_venta = (
                                    (datos_venta).customer_name,               
                                    (datos_venta).fecha_venta,
                                    ROW(array_append((array_remove(((datos_venta).discos_vendidos).articulos_comprados,'{valor_array}')),'{valor_array}'))::items_purchased
                                    )::sale_info
                                    WHERE id = {user} AND (SELECT count(titulo)
                                    FROM discos 
                                    WHERE titulo LIKE '{valor_array}') > 0;"""
                            else:
                                print("\nEl valor no puede estar vacio.")
                                continue
                        else:
                            print("\nDebe ingresar una accion valida...")
                            continue
                    else:
                        print("\nDebe ingresar un campo valido, vuelve a intentar...")
                        continue
                    cursor = db.cursor()
                    cursor.execute(command)
                    db.commit()
                    if cursor.rowcount > 0:
                        print(f"\n'{campo_string}' actualizado correctamente.")
                    else:
                        if accion == "2":
                            print(f"\n'{campo_string}' no se pudo actualizar.")
                        else:
                            print(f"\n'{campo_string}' no se pudo actualizar,\n el disco ingresado no existe.")
                    cursor.close()
                else:
                    print("\nEl ID ingresado no existe.")
            elif user == "":
                print("\nSaliendo a menu principal...")
                break
            else:
                print("\nEl ID ingresado debe ser un numero entero.")
        elif campo == "":
            print("\nSaliendo al menu principal.")
            break
        else:
            print("\nDebe ingresar un campo valido.")

# =====================================================

# ==================== SUBMENUS =======================

def submenu_inserciones() -> None:
    """Funcion para mostrar opciones de
      insercion para el usuario."""
    
    SUB_MENU = """
    1. Insertar discos.
    2. Insertar artistas.
    3. Insertar venta.
    """
    while True:
        print(SUB_MENU)
        user_sub = input("\nIngrese una opcion o presione ENTER para salir: ")
        match user_sub:
            case "1":
                insertar_disco()
            case "2":
                insertar_artista()
            case "3":
                registrar_venta()
            case "":
                print("\nSaliendo a menu principal...")
                break
            case _:
                print("\nDebe ingresar una opcion valida.")

def submenu_borrado() -> None:
    """Funcion para mostrar opciones
    de borrado para el usuario."""
    SUB_MENU = """
    1. Eliminar discos.
    2. Eliminar artistas.
    3. Eliminar ventas.
    """
    while True:
        print(SUB_MENU)
        user_sub = input("\nIngrese una opcion o presione ENTER para salir: ")
        match user_sub:
            case "1":
                eliminar_disco()
            case "2":
                eliminar_artista()
            case "3":
                eliminar_venta()
            case "":
                print("\nSaliendo a menu principal...")
                break
            case _:
                print("\nDebe ingresar una opcion valida.")


def submenu_actualizaciones() -> None:
    """Funcion para mostrar opciones de
    actualizacion para el usuario."""
    SUB_MENU = """
    1. Actualizar informacion de discos.
    2. Actualizar informacion de ventas.
    """
    while True:
        print(SUB_MENU)
        user_sub = input("\nIngrese una opcion o presione ENTER para salir: ")
        match user_sub:
            case "1":
                actualizar_disco()
            case "2":
                actualizar_venta()
            case "":
                print("\nSaliendo a menu principal...")
                break
            case _:
                print("\nDebe ingresar una opcion valida.")

def submenu_consultas() -> None:
    """Funcion para mostrar opciones de 
    consultas para el usuario."""
    SUB_MENU = """
    1. ¿Qué discos incluyen un género musical específico? 
    2. ¿Qué discos ha comprado un cliente determinado? 
    3. ¿Cuáles son los artistas que han colaborado en un disco específico? 
    """
    while True:
        print(SUB_MENU)
        user_sub = input("\nIngrese una opcion o presione ENTER para salir: ")
        match user_sub:
            case "1":
                consulta_genero_especifico()
            case "2":
                consulta_cliente_determinado()
            case "3":
                consulta_artistas_disco_colaborado()
            case "":
                print("\nSaliendo a menu principal...")
                break
            case _:
                print("\nDebe ingresar una opcion valida.")

# ===========================================================

if __name__ == '__main__':

    

    MENU = """\n    1. Crear registros.
    2. Consultar registros.
    3. Actualizar registros.
    4. Eliminar registros.
    5. Salir.\n"""
    try:
        db = conexion()
        crear_tablas(db)
        while True:
            try:
                print(MENU)
                user = input("\nIngrese una opcion: ")
                match user:
                    case "1":
                        submenu_inserciones()
                    case "2":
                        submenu_consultas()
                    case "3":
                        submenu_actualizaciones()
                    case "4":
                        submenu_borrado()
                    case "5":
                        print("\nSaliendo del programa!\n")
                        db.close()
                        break
            except psycopg2.IntegrityError as error:
                print(f"\nError de integridad: {error}")
                db.rollback()
            except Exception as error:
                print(f"\nError: {error}")
    except psycopg2.OperationalError as error:
        print(f"\nFallo al conectar con la base de datos: {error}")
    except Exception as error:
        print(f"Otro error: {error}")