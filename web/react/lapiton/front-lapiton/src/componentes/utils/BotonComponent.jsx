import React from 'react'
import "../css/BotonComponent.css"
function BotonComponent(props) {

  async function obtenerUsuario(nombreUsuario){
    try {
      const peticion = {
      method: "GET",
    }
      const response = await fetch("http://127.0.0.1:5000/registrar/usuarios?username="+nombreUsuario,peticion);
      
      if (response.ok) {
        console.log("Exito");
        const datos = await response.json();  
        console.log(datos);
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  function validarCampos(usuario,contraseña,contraseñaRepetida){
    let mensaje = "";
    if(usuario.length < 4){
      mensaje = "El nombre de usuario debe tener 4 o mas caracteres.";
    }else if(contraseña.length < 8){
      mensaje = "La contraseña debe tener 8 o mas caracteres.";
    }else if(contraseña != contraseñaRepetida){
      mensaje = "Las contraseñas no coinciden."
    }
    const usuarioResponse = obtenerUsuario(usuario).then(datos => {
      if(datos.nombre==usuario){
        mensaje = "El nombre de usuario ya existe."
      }
    });
    
    return mensaje;
  }

  function registrarUsuario(){
    let usuario = document.querySelector("#usuario").value;
    let contraseña = document.querySelector("#contraseña").value;
    let contraseñaRepetida = document.querySelector("#repetir-contraseña").value;
    console.log("Valido:"+" "+validarCampos(usuario,contraseña,contraseñaRepetida));
  }
  return (
    <input type="button" onClick={registrarUsuario} value={props.value} id={props.id} className={props.className} />
  )
}

export default BotonComponent;