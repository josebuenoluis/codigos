import React from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import "../css/PreguntasComponent.css"


function PreguntasComponent() {

    async function obtenerPreguntas(){
        try{
          const peticion = {
            method: "GET",
          };
          const response = await fetch("http://lapiton.zapto.org:5000/preguntas",peticion)
    
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

      const preguntas = obtenerPreguntas().then(datos =>{
        let seccion = document.querySelector(".seccion-principal")
        for(var pregunta in datos){
          let objetoPregunta = datos.at(pregunta)
          let articlePregunta = document.createElement("article")
          articlePregunta.style.gridColumnStart = "1";
          articlePregunta.style.gridColumnEnd = "-1";
          articlePregunta.style.display = "flex";
          articlePregunta.style.flexDirection = "column";
          articlePregunta.className = "article-pregunta"
          articlePregunta.onclick = mostrarPregunta
          let contenedorPregunta = document.createElement("div")
          contenedorPregunta.className = "contenedor-pregunta"
          let contenedorBotonMostrar = document.createElement("div")
          contenedorBotonMostrar.className = "contenedor-icono-mostrar"
          contenedorBotonMostrar.style.marginRight = "2rem"
          let imagen = document.createElement("img")
          imagen.src = "src/assets/flecha-hacia-abajo-icon.png"
          contenedorBotonMostrar.appendChild(imagen)
          let tituloPregunta = document.createElement("p")
          tituloPregunta.textContent = objetoPregunta.pregunta
          let respuesta = document.createElement("p")
          respuesta.textContent = objetoPregunta.respuesta
          respuesta.className = "respuesta-texto"
          respuesta.style.display = "none"
          contenedorPregunta.appendChild(tituloPregunta)
          contenedorPregunta.appendChild(contenedorBotonMostrar)
          articlePregunta.appendChild(contenedorPregunta)
          articlePregunta.appendChild(respuesta)
          seccion.appendChild(articlePregunta)
        }
      })

      function mostrarPregunta(e){
        let articleSeleccionado = e.target.closest("article")
        console.log(articleSeleccionado)
        let respuestaMostrar = articleSeleccionado.querySelector(".respuesta-texto")
        let iconoFlecha = articleSeleccionado.querySelector(".contenedor-pregunta .contenedor-icono-mostrar img")
        console.log(respuestaMostrar)
        if(respuestaMostrar.style.display == "none"){
          respuestaMostrar.style.display = ""
          iconoFlecha.style.transform = "scaleY(-1)"
        } else{
          respuestaMostrar.style.display = "none"
          iconoFlecha.style.transform = "scaleY(1)"

        }
      }


  return (
    <div className="container-principal">
      <HeaderComponent />
      <section className="seccion-principal">
        <article className="article-titulo-preguntas">
          <p className="titulo-preguntas">Preguntas frecuentes</p>
          <hr />
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default PreguntasComponent;
