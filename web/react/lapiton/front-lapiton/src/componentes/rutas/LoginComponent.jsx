import React from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import InputTextComponent from "../utils/InputTextComponent";
import BotonComponent from "../utils/BotonComponent";
import { useNavigate } from "react-router-dom";
import { userContext } from "../../context/userContext";
import { useContext } from "react";
import "../css/LoginComponent.css";
import VentanaAgregarComponent from "./VentanaAgregarComponent";
function LoginComponent() {
  const navigate = useNavigate()
  const {user,setUser,loginUsuario,setLocalStorage} = useContext(userContext)
  async function obtenerUsuario(nombreUsuario, contraseña) {
    try {
      const peticion = {
        method: "GET",
      };
      const response = await fetch(
        `http://lapiton.zapto.org:5000/login/usuarios?username=${nombreUsuario}&password=${contraseña}`,
        peticion
      );

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
    function registro() {
      navigate("/registro");
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
      let panel = document.querySelector(".panel-inicio-sesion")
      let seccion = document.querySelector("#seccion-principal")
      seccion.appendChild(ventana)
    }

    function iniciarSesion() {
      let usuario = document.querySelector("#usuario").value;
      let contraseña = document.querySelector("#contraseña").value;
      const usuarioResponse = obtenerUsuario(usuario, contraseña).then(
        datos => {
          debugger
          if (datos.valido) {
            console.log("Usuario encontrado");
            let tiempoActual = new Date().getTime()
            debugger
            setLocalStorage({"nombre":datos.nombre,"avatar":datos.avatar,"tiempo":tiempoActual,"clave":contraseña})
            navigate("/");
          } else {
            console.log("Usuario o contraseña son incorrectos");
            ventanaEmergente("Usuario o contraseña son incorrectos","src/assets/user-icon-red.svg");
          }
        }
      );
    }

    return (
      <div id="container-principal">
        <HeaderComponent />
        <section id="seccion-principal">
          <article className="article-titulo-iniciar-sesion">
            <p>Iniciar sesión</p>
            <hr />
          </article>
          <article className="article-inicio-sesion">
            <div className="panel-inicio-sesion">
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
              <InputTextComponent
                type={"text"}
                id={"usuario"}
                className={"text-component"}
                placeholder={"Nombre de usuario..."}
              />
              <InputTextComponent
                type={"password"}
                id={"contraseña"}
                className={"text-component"}
                placeholder={"Contraseña."}
              />
              <BotonComponent
                id={"confirmar"}
                value={"Confirmar"}
                className={"boton-component"}
                funcion={iniciarSesion}
              />
              <BotonComponent
                id={"btn-registro-iniciar"}
                value={"Registrarse"}
                className={"boton-component"}
                funcion={registro}
              />
            </div>
          </article>
        </section>
        <FooterComponent />
      </div>
    );
  }

export default LoginComponent;
