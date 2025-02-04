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
          const response = await fetch("http://lapiton.zapto.org:5000/preguntas/",peticion)
    
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
      })

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
