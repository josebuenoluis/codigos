import React from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import InputTextComponent from "../utils/InputTextComponent";
import BotonRegistroComponent from "../utils/BotonRegistroComponent";
import BotonComponent from "../utils/BotonComponent";
import "../css/RegistroComponent.css";
function RegistroComponent() {

  function iniciarSesion(){
    window.location.href = "/login"
  }
  
  async function consultarAvatares(){
    try {
      const peticion = {
      method: "GET",
    }
      const response = await fetch("http://127.0.0.1:5000/registrar/avatars");
      if (response.ok) {
        console.log("Exito");
        debugger
        const datos = await response.json();  
        debugger
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  function mostrarAvatars(){
    const resultado = consultarAvatares().then(datos =>{
      debugger
      let lista = document.querySelector("#lista-avatares");
      for(let pos in datos){
        let avatar = datos.at(pos);
        let listaItem = document.createElement("li");
        let imagen = document.createElement("img");
        imagen.src = avatar.imagen;
        imagen.width = "50";
        imagen.height  = "50";
        listaItem.appendChild(imagen);
        lista.appendChild(listaItem);
      }
    });
  }

  return (
    <div>
      <HeaderComponent />

      <section>
        <article className="article-titulo-registro">
          <p>Registro de usuario</p>
          <hr />
        </article>
        <article className="article-panel-registro">
          <div className="panel-registro">
            <svg
              width="76"
              height="73"
              viewBox="0 0 76 73"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M75.5 37.5C75.5 56.7985 58.7433 72.5 38 72.5C17.2567 72.5 0.5 56.7985 0.5 37.5C0.5 18.2015 17.2567 2.5 38 2.5C58.7433 2.5 75.5 18.2015 75.5 37.5Z"
                fill="white"
                stroke="black"
              />
              <path
                d="M38.5002 11.8333C41.6386 11.8333 44.6484 13.0801 46.8676 15.2992C49.0868 17.5184 50.3335 20.5283 50.3335 23.6667C50.3335 26.8051 49.0868 29.8149 46.8676 32.0341C44.6484 34.2533 41.6386 35.5 38.5002 35.5C35.3618 35.5 32.3519 34.2533 30.1327 32.0341C27.9136 29.8149 26.6668 26.8051 26.6668 23.6667C26.6668 20.5283 27.9136 17.5184 30.1327 15.2992C32.3519 13.0801 35.3618 11.8333 38.5002 11.8333ZM38.5002 41.4167C51.576 41.4167 62.1668 46.7121 62.1668 53.25V59.1667H14.8335V53.25C14.8335 46.7121 25.4243 41.4167 38.5002 41.4167Z"
                fill="black"
              />
            </svg>
            <BotonComponent id={"btn-mostrar"} value={"Mostrar avatares"} className={"boton-component"} funcion={mostrarAvatars}/>
            <ul id="lista-avatares">

            </ul>
            <InputTextComponent type={"text"} id={"usuario"} className={"text-component"} placeholder={"Nombre de usuario..."} />
            <InputTextComponent type={"password"} id={"contraseña"} className={"text-component"} placeholder={"Contraseña."} />
            <InputTextComponent type={"password"} id={"repetir-contraseña"} className={"text-component"} placeholder={"Repetir contraseña."} />
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
