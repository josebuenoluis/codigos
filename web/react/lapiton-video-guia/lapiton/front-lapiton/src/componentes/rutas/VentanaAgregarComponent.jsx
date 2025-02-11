import React from 'react'
import "../css/VentanaAgregarComponent.css"
import imagenInsertar from "../../assets/inserteImagen.png"
import HeaderComponent from '../header/HeaderComponent'
import FooterComponent from '../footer/FooterComponent'
import InputTextComponent from '../utils/InputTextComponent'
import BotonComponent from '../utils/BotonComponent'
import DescripcionComponent from '../utils/DescripcionComponent'
import SelectorArchivos from '../utils/SelectorArchivosComponent'
import { useNavigate } from "react-router-dom";

function VentanaAgregarComponent() {

    const navigate = useNavigate()

    // Funcion que se llamara cada vez que el usuario selecciona una imagen
    // para una novedad
    function obtenerImagen(e){
        let img = document.querySelector("#img-novedad");
        let file = document.querySelector("#id-selector");
        // Si selecciono alguna imagen la obtenemos y la mostraremos
        if(e.target.files[0]){
            const reader = new FileReader()
            reader.onload = function(e){
                img.src = e.target.result
            }
            let base = e.target.files[0]
            reader.readAsDataURL(e.target.files[0])
        }else{
            img.src = imagenInsertar
        }
    }

    // Funcion para obtener los datos de la novedad ingresados por el usuario
    function obtenerNovedad(){
        let titulo = document.querySelector("#titulo").value
        let img = document.querySelector("#img-novedad").src;
        let descripcion = document.querySelector("#descripcion").value
        let novedad = {"titulo":titulo,"imagen":img,"descripcion":descripcion}
        return novedad
    }

    // Funcion para guardar la novedad en la base de datos mediante la API
    async function subirNovedad(){
        let novedad = obtenerNovedad()
        try {
          const response = await fetch("http://lapiton.zapto.org:5000/novedades/agregar", {
            // Definimos el metodo que vamos a utilizar GET,POST,PUT,DELETE,etc...
            method: "POST",
            //Definimos un headers que sera el tipo de dato que vamos a enviar
            headers: { "Content-Type": "application/json" },
            //Agregamos el contenido que vamos a enviar
            body: JSON.stringify(novedad),
          });
          if (response.ok) {
            let jsonResponse = JSON.stringify(novedad);
            console.log(jsonResponse);
            const datos = await response.json();
            if(datos.subida==true){
              ventanaEmergente("Novedad subida con exito.","src/assets/check-green.svg","rgb(20, 174, 92)")
            }else{
              ventanaEmergente("Ya existe este titulo","src/assets/warning-icon.svg","rgb(236, 111, 111)")
            }
          }
        } catch (error) {
          console.log(error);
        }
      }

      function cerrarVentana(e){
        let seccion = document.querySelector("#seccion-principal")
        let ventana = document.querySelector(".container-ventana")
        seccion.removeChild(ventana)
      }
  
      function ventanaEmergente(mensaje,imagen,color){
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
        parrafo.style.color = color;
        contenedorMensaje.appendChild(imagenVentana);
        contenedorMensaje.appendChild(parrafo);
        ventana.appendChild(contenedorMensaje);
        let panel = document.querySelector(".panel-inicio-sesion")
        let seccion = document.querySelector("#seccion-principal")
        seccion.appendChild(ventana)
      }

      function volver(){
        navigate("/novedades")
      }

  return (
    <div>
        <HeaderComponent />
        <section id='seccion-principal'>
          <article className="article-titulo-agregar">
            <p>Agregar novedad</p>
            <hr />
          </article>
          <article className="article-agregar">
            <div className="panel-agregar">
                <div className="icono-imagen">
                    <img id="img-novedad" src={imagenInsertar} alt="Imagen Novedad" />
                </div>
                <SelectorArchivos id={"id-selector"} funcion={obtenerImagen} className={"selector-archivos"} />
                <InputTextComponent
                type={"text"}
                id={"titulo"}
                className={"text-component"}
                placeholder={"Titulo de novedad..."}
              />
                <DescripcionComponent placeholder={"Ingrese una descripción..."}
                 id={"descripcion"} />
                <BotonComponent
                id={"subir-novedad"}
                value={"Subir novedad"}
                className={"boton-component"}
                funcion={subirNovedad} />
                <BotonComponent
                id={"btn-volver"}
                value={"Volver"}
                className={"boton-component"}
                funcion={volver} />

            </div>
          </article>
        </section>
        <FooterComponent />
    </div>
  )
}

export default VentanaAgregarComponent