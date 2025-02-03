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

  const { novedad, SetNovedad, Vibrando, SetVibrando,user } =
    useContext(userContext);
    function cerrarVentana(e){
      let seccion = document.querySelector(".seccion-principal")
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
      let seccion = document.querySelector(".seccion-principal")
      seccion.appendChild(ventana)
    }
  function ventanaAgregar() {
    if(user.nombre=="admin"){
      navigate("/agregar");
    }else{
      ventanaEmergente("Debe ser usuario admin para agregar novedades","src/assets/user-icon-red.svg")
    }
  }

  function ventanaEliminar() {
    if(user.nombre=="admin"){
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
    }else{
      ventanaEmergente("Debe ser usuario admin para eliminar novedades","src/assets/user-icon-red.svg")
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
      const response = await fetch(`http://lapiton.zapto.org/novedades/eliminar?titulo=${titulo}&clave=${user.clave}`, peticion);

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
      const response = await fetch("http://lapiton.zapto.org:5000/novedades", peticion);

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
