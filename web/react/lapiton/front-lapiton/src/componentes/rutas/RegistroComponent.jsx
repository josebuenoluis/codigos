import React from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import InputTextComponent from "../utils/InputTextComponent";
import BotonRegistroComponent from "../utils/BotonRegistroComponent";
import BotonComponent from "../utils/BotonComponent";
import UserIcon from "../../assets/user-icon.svg"
import Serpiente from "../../assets/serpiente.svg"
import "../css/RegistroComponent.css";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import CheckBoxComponent from "../utils/CheckBoxComponent";
function RegistroComponent() {

  const navigate = useNavigate();

  function iniciarSesion(){
    navigate("/login");
  }
  
  async function consultarAvatares(){
    try {
      const peticion = {
      method: "GET",
    }
      const response = await fetch("http://127.0.0.1:5000/registrar/avatars");
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

  function elegirAvatar(e){
    let icono = document.querySelector("#img-avatar");
    debugger
    let iconoSeleccionado = e.target
    console.log("Cambiando avatar ","Fondo: ",iconoSeleccionado.src);
    debugger
    if(icono.src!=iconoSeleccionado.src){
      icono.src = iconoSeleccionado.src;
    }else{
      icono.src = UserIcon
    }
  }

  function mostrarAvatars(){
    const resultado = consultarAvatares().then(datos =>{
      let lista = document.querySelector("#lista-avatares");
      let carga = document.querySelector(".carga");
      lista.removeChild(carga);
      for(let pos in datos){
        let avatar = datos.at(pos);
        let listaItem = document.createElement("li");
        let imagen = document.createElement("img");
        imagen.src = avatar.imagen;
        imagen.className = "avatares-seleccionar"; 
        imagen.onclick = elegirAvatar;
        listaItem.appendChild(imagen);
        lista.appendChild(listaItem);

      }
    });
  }
  mostrarAvatars()
  return (
    <div>
      <HeaderComponent />

      <section id="seccion-principal">
        <article className="article-titulo-registro">
          <p>Registro de usuario</p>
          <hr />
        </article>
        <article className="article-panel-registro">
          <div className="panel-registro">
            <div className="icono-avatar">
              <div id="avatar">
                <img id="img-avatar" src={UserIcon} alt="Icon" />
              </div>
            <ul id="lista-avatares">
              <div className="carga">
                <img id="serpiente-carga" src={Serpiente} alt="Icon" />
                <span id="texto-carga">Cargando avatares...</span>
              </div>
            </ul>
          </div>
            
            <InputTextComponent type={"text"} id={"usuario"} className={"text-component"} placeholder={"Nombre de usuario..."} />
            <InputTextComponent type={"password"} id={"contraseña"} className={"text-component"} placeholder={"Contraseña."} />
            <InputTextComponent type={"password"} id={"repetir-contraseña"} className={"text-component"} placeholder={"Repetir contraseña."} />
            <CheckBoxComponent id={"id-check"} name={"terminos"} label={"Terminos y condiciones."} />
            <BotonRegistroComponent id={"confirmar"} value={"Confirmar"} className={"boton-component"} />
            <BotonComponent id={"btn-inicio-registro"} value={"Iniciar sesion"} className={"boton-component"} funcion={iniciarSesion}/>
          </div>
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default RegistroComponent;
