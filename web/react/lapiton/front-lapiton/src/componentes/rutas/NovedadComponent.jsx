import React from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import { userContext } from "../../context/userContext";
import { useContext } from "react";
import "../css/NovedadComponent.css"


function NovedadComponent() {
    
    const {novedad,SetNovedad} = useContext(userContext)
    debugger
    console.log(novedad)

    async function obtenerNovedad(titulo) {
    try {
      const peticion = {
        method: "GET",
      };
      const response = await fetch(
        `http://lapiton.zapto.org:5000/novedades/novedad?titulo=${titulo}`,
        peticion
      );

      if (response.ok) {
        console.log("Exito");
        debugger
        const datos = await response.json();
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  const juegos = obtenerNovedad(novedad).then((datos) => {
    let titulo = document.querySelector(".titulo-novedad");
    let imagen = document.querySelector("#imagen-novedad");
    let descripcion = document.querySelector(".descripcion-novedad");
    titulo.textContent = datos.titulo
    imagen.src = datos.imagen
    descripcion.textContent = datos.descripcion
  });

  return (
    <div>
      <HeaderComponent />
      <section>
        <article className="article-titulo-novedad">
          <p className="titulo-novedad"></p>
          <hr />
        </article>
        <article className="article-novedad">
          <div className="contenedor-novedad">
            <div className="container-imagen">
                <img src="" id="imagen-novedad" alt="" />
            </div>
            <p className="descripcion-novedad"></p>
            
          </div>
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default NovedadComponent;
