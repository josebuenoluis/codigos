import React from "react";
import { Link } from "react-router-dom";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import DesplegableComponent from "../utils/DesplegableComponent";
import BarraBusqueda from "../utils/BarraBusqueda";
import BotonAgregar from "../utils/BotonAgregarComponent";
import BotonEliminarComponent from "../utils/BotonEliminarComponent";
import "../css/NovedadesComponent.css";
import { useNavigate } from "react-router-dom";

function Novedades() {
  const navigate = useNavigate()
  
  function ventanaAgregar(){
    navigate("/agregar")
  }

  function ventanaEliminar(){
    alert("ventanaEliminar");
  }

  async function obtenerNovedades() {
    try {
      const peticion = {
        method: "GET",
      };
      const response = await fetch("http://127.0.0.1:5000/novedades", peticion);

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

  const juegos = obtenerNovedades().then((datos) => {
    let section = document.querySelector(".seccion-principal");
    for (var juego in datos) {
      let articuloJuego = document.createElement("article");
      articuloJuego.className = "article-contenido";
      let enlace = document.createElement("a");
      enlace.href = "/novedades";
      let objeto = datos.at(juego);
      let contenedor = document.createElement("div");
      contenedor.className = "novedad";
      let imagen = document.createElement("img");
      imagen.alt = "fondo-novedad";
      imagen.src = objeto.imagen;
      let titulo = document.createElement("p");
      titulo.textContent = objeto.titulo;
      contenedor.appendChild(imagen);
      contenedor.appendChild(titulo);
      enlace.appendChild(contenedor);
      articuloJuego.appendChild(enlace);
      section.appendChild(articuloJuego);
    }
  });

  return (
    <div>
      <HeaderComponent />
      <section className="seccion-principal">
        <article className="article-categoria">
          <p>Novedades</p>
          <hr />
        </article>
        <article className="article-agregar-eliminar">
          <div className="botones">
            <BotonAgregar id={"id-btn-agregar"} funcion={ventanaAgregar} className={"btn-agregar"} />
            <BotonEliminarComponent
              id={"id-btn-eliminar"}
              className={"btn-eliminar"}
              funcion={ventanaEliminar}
            />
          </div>
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default Novedades;
