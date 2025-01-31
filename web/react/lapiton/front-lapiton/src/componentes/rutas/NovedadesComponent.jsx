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
import { useContext, useState } from "react";
import { userContext } from "../../context/userContext";

function Novedades() {
  const navigate = useNavigate();

  const { novedad, SetNovedad, Vibrando, SetVibrando } =
    useContext(userContext);

  function ventanaAgregar() {
    navigate("/agregar");
  }

  function ventanaEliminar() {
    let divs = document.querySelectorAll(".novedad");
    let section = document.querySelector(".seccion-principal");
    let vibracion = false;
    debugger;
    if (Vibrando == false) {
      for (var div in divs) {
        let novedad = divs.item(div);
        if (novedad.className == "novedad") {
          novedad.onclick = eliminarNovedad;
          novedad.classList.add("vibracion");
        }
      }
      SetVibrando(true);
    } else {
      let articles = section.querySelectorAll(".article-contenido");
      articles.forEach((article) => {
        section.removeChild(article);
      });
      SetVibrando(false);
    }
  }

  function eliminarNovedad(e) {
    let section = document.querySelector(".seccion-principal");
    let articleNovedad = e.target.closest("article");
    let titulo = articleNovedad.querySelector("p").textContent;
    debugger
    SetNovedad(titulo);
    peticionEliminar(titulo).then(datos =>{
      if(datos.realizada==true){
        console.log("Novedad eliminada:", titulo);
        if (articleNovedad) {
          section.removeChild(articleNovedad);
        }
      }else{
        console.log("Fallo al eliminar:", titulo);
      }
    })
  }


  async function peticionEliminar(titulo) {
    try {
      const peticion = {
        method: "DELETE",
      };
      const response = await fetch(`http://127.0.0.1:5000/novedades/eliminar?titulo=${titulo}`, peticion);

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

  function mostrarNovedad(e) {
    let titulo = e.currentTarget.querySelector("p").textContent;
    debugger;
    console.log(novedad);
    SetNovedad(titulo);
    console.log(novedad);
    navigate("/novedades/novedad");
  }

  const juegos = obtenerNovedades().then((datos) => {
    let section = document.querySelector(".seccion-principal");
    if (Vibrando == false && section.childNodes.length <= 2) {
      for (var juego in datos) {
        let articuloJuego = document.createElement("article");
        articuloJuego.className = "article-contenido";
        let objeto = datos.at(juego);
        let contenedor = document.createElement("div");
        contenedor.className = "novedad";
        contenedor.onclick = mostrarNovedad;
        let imagen = document.createElement("img");
        imagen.alt = "fondo-novedad";
        imagen.src = objeto.imagen;
        let titulo = document.createElement("p");
        titulo.textContent = objeto.titulo;
        contenedor.appendChild(imagen);
        contenedor.appendChild(titulo);
        articuloJuego.appendChild(contenedor);
        section.appendChild(articuloJuego);
      }
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
            <BotonAgregar
              id={"id-btn-agregar"}
              funcion={ventanaAgregar}
              className={"btn-agregar"}
            />
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
