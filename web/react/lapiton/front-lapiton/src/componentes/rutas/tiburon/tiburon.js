
let velocidadEnemigo = 1500;
let puntaje = 0;
let bola = document.querySelector(".bola");
let campo = document.querySelector(".campo");
let puntos = document.querySelector("#puntos");
let dificultadText = document.querySelector("#dificultad");
puntos.textContent = puntaje;
let posicionX = 1;
let posicionY = 1;
let direccion = 1;
let rightPressed = false;
let leftPressed = false;
let downpressed = false;
let uppressed = false;
let posicionEnemigoX = 0;
let posicionEnemigoY = 0;
let listaLadrillos = [];
let interval = 0;
let dificultad = 0;
let nivel = document.querySelector("#dificultad");
let juegoIniciado = false;
let segundos = 0;
let ventanActivada = false;
nivel.textContent = dificultad;


// Funcion para contar el timepo que dura el jugador
function reloj() {
  segundos += 1;
  console.log(segundos);
}

// Definimos los cursores del usuario
document.addEventListener("keydown", keyDownHandler, false); // Le decimos al DOM que escuche cuando el usuario pulse la tecla derecha
document.addEventListener("keyup", keyUpHandler, false); // Le decimos al DOM que escuche cuando el usuario pulse la tecla izquierda



// Creamos una funcion que se activara cuando el usuario pulse la tecla especificada en el addEventListener
function keyDownHandler(e) {
  console.log("Evento: "+e);
  if (e.keyCode == 39) {
    //console.log("derecha") // He añadido esta linea para comprobar en la consola que se activa la funcion
    // al pulsar la tecla derecha
    rightPressed = true;
    moverDerecha();
    e.preventDefault(); 
  } else if (e.keyCode == 40) {
    moverAbajo();
    e.preventDefault(); 
    downpressed = true;
  } else if (e.keyCode == 38) {
    uppressed = true;
    moverArriba();
    e.preventDefault(); 
  } else if (e.keyCode == 37) {
    leftPressed = true;
    moverIzquierda();
    e.preventDefault(); 
  } else if (e.keyCode == 32) {
    console.log("inicio");
    iniciarJuego();
    e.preventDefault(); 
  }
}


function keyUpHandler(e) {
  console.log("Evento: "+e.keyCode);
  if (e.keyCode == 39) {
    rightPressed = false;
    detectarColision();
  } else if (e.keyCode == 40) {
    downpressed = false;
    detectarColision();
  } else if (e.keyCode == 38) {
    uppressed = false;
    detectarColision();
  } else if (e.keyCode == 37) {
    leftPressed = false;
    detectarColision();
  }
}

// Estado inicial
let estadoInicial = function () {
  let mensaje = document.createElement("div");
  mensaje.className = "mensaje";
  mensaje.classList.add("mensaje");
  campo.appendChild(mensaje);
  mensaje.style.width = "21.87rem";
  mensaje.style.height = "9.37rem";
  mensaje.style.borderRadius = "1.25rem";
  mensaje.style.border = "5px solid black";
  mensaje.style.gridColumnStart = 3;
  mensaje.style.gridRowStart = 4;
  mensaje.style.background = "white";
  mensaje.style.display = "flex";
  mensaje.style.alignItems= "center";
  mensaje.style.justifyContent = "center";
  let texto = document.createElement("p");
  texto.style.font = "1.25rem";
  texto.style.textAlign = "center";
  texto.style.verticalAlign = "center";
  texto.style.fontWeight = "bold";
  texto.textContent = "PRESIONE SPACE BAR PARA COMENZAR";
  texto.style.fontFamily = "Arial, Helvetica, sans-serif";
  mensaje.appendChild(texto);
};
estadoInicial();

//Ventana para volver a empezar y guardar progreso
function ventanaRegresar() {
  if (juegoIniciado == true) {
    juegoIniciado = false;
    ventanActivada = true;
    // Creacion de ventana para volver a jugar y guardar datos de progreso del usuario
    let ventana = document.createElement("div");
    ventana.className = "ventana";
    ventana.classList.add("ventana");
    ventana.style.display = "flex";
    ventana.style.flexDirection = "column";
    ventana.style.justifyContent = "space-between";
    ventana.style.alignItems = "center";
    campo.appendChild(ventana);
    ventana.style.width = "15rem";
    ventana.style.height = "15rem";
    ventana.style.gridColumnStart = 4;
    ventana.style.gridRowStart = 3;
    ventana.style.background = "white";
    ventana.style.background = "#ccc";
    ventana.style.borderRadius = "20px";
    ventana.style.alignItems = "center";
    ventana.style.justifyContent = "center";
    ventana.style.border = "5px solid black";

    // Creacion de input para guardar progreso del usuario en la base de datos
    let guardar = document.createElement("input");
    guardar.type = "submit";
    guardar.style.width = "10.62rem";
    guardar.style.height = "3.125rem";
    guardar.style.margin = "auto";
    guardar.style.fontSize = "1.25rem";
    guardar.style.fontWeight = "bold";
    guardar.style.borderRadius = "10px";
    guardar.style.fontSize = "1.25rem";
    guardar.style.fontFamily = "Cherry Bomb One";
    guardar.style.fontWeight = "400";
    guardar.style.fontStyle = "normal";
    guardar.value = "Guardar puntos";
    guardar.addEventListener("click", post);
    ventana.appendChild(guardar);
    // Creacion del boton para volver a jugar
    let volver = document.createElement("input");
    volver.type = "button";
    volver.style.width = "10.625rem";
    volver.style.height = "3.125rem";
    volver.style.margin = "auto";
    volver.style.fontWeight = "bold";
    volver.value = "Volver a Jugar";
    volver.style.fontSize = "1.25rem";
    volver.style.fontFamily = "Cherry Bomb One";
    volver.style.fontWeight = "400";
    volver.style.fontStyle = "normal";
    volver.style.borderRadius = "0.625rem";
    volver.addEventListener("click", regresar);
    ventana.appendChild(volver);
  }
}

// Funcion para guardar los datos del usuario en la base de datos
function crearUsuario() {
  // Limpiamos el input de texto del nombre de usuario
  console.log("DATOS GUARDADOS.");
  let user = JSON.parse(window.localStorage.getItem("puntaje"));

  // let nombreUsuario = document.querySelector("#nombre").value;
  // let puntosUsuario = puntaje;
  // let dificultadUsuario = dificultad;
  // //Creamos objeto de JavaScript Usuario
  // let usuario = {
  //   nombre: nombreUsuario,
  //   puntos: puntosUsuario,
  //   dificultad: dificultadUsuario,
  // };
  console.log(user);
  // Creamos la peticion de fetch
  // La peticion FECTH recibe 2 argumentos: ('url',{method:"",contenido= headers:"Content-Type:=''",body:formato-headers=contenido})
  return user;
}

const post = async () => {
  let usuario = crearUsuario();
  console.log("Dentro de post: ",usuario);
  try {
    const response = await fetch("http://127.0.0.1:5000/ranking/puntos", {
      // Definimos el metodo que vamos a utilizar GET,POST,PUT,DELETE,etc...
      method: "POST",
      //Definimos un headers que sera el tipo de dato que vamos a enviar
      headers: { "Content-Type": "application/json" },
      //Agregamos el contenido que vamos a enviar
      body: JSON.stringify(usuario),
    });
    if (response.ok) {
      let jsonResponse = JSON.stringify(usuario);
      console.log(jsonResponse);
    }
  } catch (error) {
    console.log(error);
  }
};

function regresar() {
  puntaje = 0;
  dificultad = 0;
  velocidadEnemigo = 1500;
  nivel.textContent = dificultad;
  puntos.textContent = puntaje;
  clearInterval(reloj);
  let ventana = document.querySelector(".ventana");
  juegoIniciado = false;
  ventanActivada = false;
  ventana.remove(campo);
  let ladrillo = document.querySelector(".ladrillo");
  let enemigo = document.querySelector(".enemigo");
  estadoInicial();
  ladrillo.remove(campo);
  enemigo.remove(campo);
}
// Funcion inicial
function iniciarJuego() {
  if (juegoIniciado == false && ventanActivada == false) {
    crearBola();
    crearLadrillo();
    crearEnemigo();
    setInterval(reloj,1000);
    // document.body.style.overflow = "hidden";
    let mensaje = document.querySelector(".mensaje");
    mensaje.remove(campo);
    intervalo = setInterval(moverEnemigo, velocidadEnemigo);
    segundos = setInterval(reloj,1000);
    juegoIniciado = true;
  } else {
    console.log("El juego ya ha sido iniciado");
  }
}

function crearBola() {
  bola = document.createElement("div");
  bola.className = "bola";
  bola.classList.add("bola");
  campo.appendChild(bola);
  bola.style.gridColumnStart = posicionX;
  bola.style.gridRowStart = posicionY;
  bola.style.width = "90px";
  bola.style.height = "60px";
  bola.style.background = "url('/src/assets/pez.svg ')";
  bola.style.backgroundRepeat = "no-repeat";
}

// Definimos la funcion para mover la bola
function moverDerecha() {
  if (posicionX < 10) {
    posicionX += 1;
    bola.style.gridColumnStart = posicionX;
    detectarColision();
  } else {
    bola.remove(campo);
    ventanaRegresar();
  }
}

function moverIzquierda() {
  if (posicionX - 1 > 0 || posicionX != 0) {
    posicionX -= 1;
    bola.style.gridColumnStart = posicionX;
    detectarColision();
  } else {
    bola.remove(campo);
    ventanaRegresar();
  }
}
function moverArriba() {
  if (posicionY - 1 > 0 || posicionY != 0) {
    posicionY -= 1;
    bola.style.gridRowStart = posicionY;
    detectarColision();
    //document.body.style.overflow = "hidden";
  } else {
    bola.remove(campo);
    ventanaRegresar();
    //document.body.style.overflow = "hidden";
  }
}

function moverAbajo() {
  if (posicionY < 10) {
    posicionY += 1;
    bola.style.gridRowStart = posicionY;
    detectarColision();
    //document.body.style.overflow = "hidden";
  } else {
    bola.remove(campo);
    ventanaRegresar();
    //document.body.style.overflow = "hidden";
  }
}

// Crear ladrillo
let crearLadrillo = function () {
  let poscicionLadrillo = Math.floor(Math.random() * 10) + 1;
  let ladrillo = document.createElement("div");
  ladrillo.className = "ladrillo";
  ladrillo.style.width = "50px";
  ladrillo.style.height = "50px";
  ladrillo.style.borderRadius = "50%";
  ladrillo.style.background = "yellow";
  ladrillo.style.gridColumnStart = poscicionLadrillo;
  ladrillo.style.gridRowStart = poscicionLadrillo;
  campo.appendChild(ladrillo);
};
// crearLadrillo();

// Funcion para detectar colision
function detectarColision() {
  let bola = document.querySelector(".bola");
  let ladrillo = document.querySelector(".ladrillo");
  if (
    bola.style.gridColumnStart == ladrillo.style.gridColumnStart &&
    bola.style.gridRowStart == ladrillo.style.gridRowStart
  ) {
    puntaje += 1;
    console.log("DETECTADA");
    if (puntaje % 2 == 0 && dificultad != 13) {
      dificultad += 1;
      nivel.textContent = dificultad;
      incrementarVelocidad();
    }
    puntos.textContent = puntaje;
    ladrillo.remove(campo);
    crearLadrillo();
  }
}
// Funcion para crear un enemigo
let crearEnemigo = function () {
  let poscicionEnemigo = Math.floor(Math.random() * 9);
  poscicionEnemigo = poscicionEnemigo * 1;
  let diferencia = poscicionEnemigo - posicionX;
  if (diferencia < 0) {
    diferencia *= -1;
  }
  while (poscicionEnemigo == posicionX && diferencia < 8) {
    poscicionEnemigo = Math.floor(Math.random() * 9);
    poscicionEnemigo = poscicionEnemigo * 1;
    diferencia = poscicionEnemigo - posicionX;
  }
  let enemigo = document.createElement("div");
  campo.appendChild(enemigo);
  enemigo.className = "enemigo";
  // enemigo.style.width = "50px";
  // enemigo.style.height = "50px";
  enemigo.style.gridColumnStart = poscicionEnemigo;
  enemigo.style.gridRowStart = poscicionEnemigo;
  enemigo.style.background = "url('/src/assets/tiburon.svg ')";
  enemigo.style.backgroundRepeat = "no-repeat";
  enemigo.style.width = "200px";
  enemigo.style.height = "90px";
};
// crearEnemigo();

// Funcion para mover enemigo
function moverEnemigo() {
  let enemigo = document.querySelector(".enemigo");
  if (posicionEnemigoX < posicionX) {
    posicionEnemigoX += 1;
  } else if (posicionEnemigoX == posicionX) {
    comer();
  } else {
    posicionEnemigoX -= 1;
  }
  if (posicionEnemigoY < posicionY) {
    posicionEnemigoY += 1;
  } else if (posicionEnemigoY == posicionX) {
    comer();
  } else {
    posicionEnemigoY -= 1;
  }
  enemigo.style.gridColumnStart = posicionEnemigoX;
  enemigo.style.gridRowStart = posicionEnemigoY;
  if (enemigo.style.gridColumnStart >= 5){
    enemigo.style.transform = "rotate(180deg)";
  }else{
    enemigo.style.transform = "rotate(0deg)";
  }
}

// Intervalo para mover enemigo
// intervalo = setInterval(moverEnemigo, velocidadEnemigo);

// Funcion para que el enemigo se coma al usuario
function comer() {
  let bola = document.querySelector(".bola");
  let enemigo = document.querySelector(".enemigo");
  if (posicionX == posicionEnemigoX && posicionY == posicionEnemigoY) {
    if (campo.contains(bola)) {
      bola.remove(campo);
      clearInterval(reloj);
      //Llamamos a la funcion para preguntar si desea guardar los puntajes y volver a empezar
      ventanaRegresar();
    }
    clearInterval(intervalo);
  }
}

// Funcion para incrementar velocidad del enemigo
function incrementarVelocidad() {
  if (velocidadEnemigo > 200) {
    velocidadEnemigo -= 100;
  }
  clearInterval(intervalo);
  intervalo = setInterval(moverEnemigo, velocidadEnemigo);
}
