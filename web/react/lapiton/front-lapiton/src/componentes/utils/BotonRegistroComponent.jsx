import React,{useContext} from 'react'
import "../css/BotonRegistroComponent.css"
import { userContext } from '../../context/userContext';
import { useNavigate } from 'react-router-dom';
function BotonComponent(props) {
  const {user,setUser,loginUsuario,setLocalStorage} = useContext(userContext)
  const navigate = useNavigate()
  async function obtenerUsuario(nombreUsuario){
    try {
      const peticion = {
      method: "GET",
    }
      const response = await fetch("http://127.0.0.1:5000/registrar/usuarios?username="+nombreUsuario,peticion);
      
      if (response.ok) {
        console.log("Exito");
        const datos = await response.json();  
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  async function crearUsuario(usuario){
    try {
      const response = await fetch("http://lapiton.zapto.org:5000/registrar/usuarios", {
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
  }

  function validarCampos(usuario,contraseña,contraseñaRepetida){
    let mensaje = "";
    if(usuario.length < 4){
      mensaje = "El nombre de usuario debe tener 4 o mas caracteres.";
    }else if(contraseña.length < 8){
      mensaje = "La contraseña debe tener 8 o mas caracteres.";
    }else if(contraseña != contraseñaRepetida){
      mensaje = "Las contraseñas no coinciden.";
    }
    return mensaje;
  }

  function registrarUsuario(){
    let usuario = document.querySelector("#usuario").value;
    let contraseña = document.querySelector("#contraseña").value;
    let avatar = document.querySelector("#img-avatar").src;
    let contraseñaRepetida = document.querySelector("#repetir-contraseña").value;
    let mensajeError = validarCampos(usuario,contraseña,contraseñaRepetida)
    let terminos = document.querySelector("#id-check");
    if(mensajeError == ""){
      if(terminos.checked){
        const usuarioResponse = obtenerUsuario(usuario).then(datos => {
          console.log("Usuario consultado: ",datos);
          if(Object.keys(datos).length==0){
            crearUsuario({"nombre":usuario,"contraseña":contraseña,"avatar":avatar});
            let tiempoActual = new Date().getTime()
            setLocalStorage({"nombre":usuario,"avatar":avatar,"tiempo":tiempoActual})
            console.log("INsertar");
            navigate("/");
          }else{
            console.log("El nombre de usuario ya existe.")
            ventanaEmergente("El nombre de usuario ya existe.","src/assets/user-icon-red.svg")
          }
        });
      }else{
        ventanaEmergente("Debe aceptar los terminos y condiciones.","src/assets/user-icon-red.svg")
      }
    }else{
      ventanaEmergente(mensajeError,"src/assets/user-icon-red.svg")
    }
  }

  function cerrarVentana(e){
    let seccion = document.querySelector("#seccion-principal")
    let ventana = document.querySelector(".container-ventana")
    seccion.removeChild(ventana)
  }

  function ventanaEmergente(mensaje,imagen){
    let ventana = document.createElement("div");
    ventana.className = "container-ventana";
    ventana.style.display = "flex";
    ventana.style.flexDirection = "column";
    ventana.style.alignItems = "center";
    ventana.style.justifyContent = "center";
    ventana.onclick = cerrarVentana;
    ventana.style.margin = "auto";
    ventana.style.position = "absolute";
    let contenedorMensaje = document.createElement("div");
    contenedorMensaje.className = "container-mensaje";
    let imagenVentana = document.createElement("img");
    imagenVentana.id = "imagen-ventana";
    imagenVentana.src = imagen;
    let parrafo = document.createElement("p")
    parrafo.id = "texto-ventana";
    parrafo.textContent = mensaje;
    parrafo.style.color ="rgb(236, 111, 111)";
    contenedorMensaje.appendChild(imagenVentana);
    contenedorMensaje.appendChild(parrafo);
    ventana.appendChild(contenedorMensaje);
    let seccion = document.querySelector("#seccion-principal")
    seccion.appendChild(ventana)
  }

  return (
    <input type="button" onClick={registrarUsuario} value={props.value} id={props.id} className={props.className} />
  )
}

export default BotonComponent;