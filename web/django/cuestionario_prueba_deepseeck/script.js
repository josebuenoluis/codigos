let preguntas = [];
let respuestasUsuario = [];

// Cargar las preguntas desde el archivo JSON
fetch('preguntas.json')
  .then(response => response.json())
  .then(data => {
    preguntas = data.preguntas;
    mostrarCuestionario();
  })
  .catch(error => console.error('Error al cargar las preguntas:', error));

// Mostrar el cuestionario en la página
function mostrarCuestionario() {
  const cuestionarioDiv = document.getElementById('cuestionario');
  preguntas.forEach((pregunta, index) => {
    const preguntaDiv = document.createElement('div');
    preguntaDiv.className = 'pregunta';
    preguntaDiv.innerHTML = `
      <h3>${index + 1}. ${pregunta.pregunta}</h3>
      <div class="opciones">
        ${pregunta.opciones.map((opcion, i) => `
          <div class="opcion">
            <input type="radio" name="pregunta${index}" value="${opcion}" id="pregunta${index}_opcion${i}">
            <label for="pregunta${index}_opcion${i}">${opcion}</label>
          </div>
        `).join('')}
      </div>
    `;
    cuestionarioDiv.appendChild(preguntaDiv);
  });
}

// Calcular el resultado del cuestionario
function calcularResultado() {
  respuestasUsuario = [];
  let aciertos = 0;

  preguntas.forEach((pregunta, index) => {
    const seleccionada = document.querySelector(`input[name="pregunta${index}"]:checked`);
    if (seleccionada) {
      respuestasUsuario.push(seleccionada.value);
      if (seleccionada.value === pregunta.respuesta_correcta) {
        aciertos++;
      }
    } else {
      respuestasUsuario.push(null);
    }
  });

  const resultadoDiv = document.getElementById('resultado');
  resultadoDiv.innerHTML = `Has acertado ${aciertos} de ${preguntas.length} preguntas.`;
}