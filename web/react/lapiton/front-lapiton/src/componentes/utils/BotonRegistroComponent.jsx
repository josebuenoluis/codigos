import React,{useContext} from 'react'
import "../css/BotonRegistroComponent.css"
import { userContext } from '../../context/userContext';
import { useNavigate } from 'react-router-dom';
function BotonComponent(props) {
  const {user,setUser,loginUsuario} = useContext(userContext)
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
      const response = await fetch("http://127.0.0.1:5000/registrar/usuarios", {
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
    if(validarCampos(usuario,contraseña,contraseñaRepetida) == ""){
      const usuarioResponse = obtenerUsuario(usuario).then(datos => {
        console.log("Usuario consultado: ",datos);
        if(Object.keys(datos).length==0){
          crearUsuario({"nombre":usuario,"contraseña":contraseña,"avatar":avatar});
          debugger
          loginUsuario({"nombre":usuario,"avatar":avatar})
          console.log("INsertar");
          navigate("/");
        }else{
          console.log("El nombre de usuario ya existe.")
        }
      });

    }
  }

  return (
    <input type="button" onClick={registrarUsuario} value={props.value} id={props.id} className={props.className} />
  )
}

export default BotonComponent;