import React,{useContext} from "react";
import { useLocation } from "react-router-dom";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import "../css/InicioComponent.css";
import FondoTiburon from "../../assets/fondoTiburonInicio.svg"
import FondoSerpiente from "../../assets/campo-serpiente-1 1.svg"
import FondoBestia from "../../assets/campo-bestia-1 1.svg"
import { Link } from "react-router-dom";
import { userContext } from "../../context/userContext";
import BarraBusqueda from "../utils/BarraBusqueda";
import { useNavigate } from "react-router-dom";

function Inicio() {
  
  const navigate = useNavigate();
  const {user,setUser} = useContext(userContext)
  const location = useLocation()
  const parametros = new URLSearchParams(location.search)
  
 async function obtenerJuegos(){
    try{
      const peticion = {
        method: "GET",
      };
      const response = await fetch("http://127.0.0.1:5000/",peticion)

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

  async function obtenerJuegosFiltros(titulo){
    try{
      const peticion = {
        method: "GET",
      };
      const response = await fetch(`http://127.0.0.1:5000/?titulo=${titulo}`,peticion)
      if (response.ok) {
        debugger
        console.log("Exito");
        const datos = await response.json();
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  function limpiarSeccion(){
    let section = document.querySelector(".seccion-principal");
    let articleJuegos = section.querySelectorAll(".article-juegos");
    articleJuegos.forEach((juego) => {
      section.removeChild(juego);
    });
    let articleCategorias = section.querySelectorAll(".article-categoria");
    articleCategorias.forEach((categoria) => {
        section.removeChild(categoria);
      });
  }

  function obtenerJuegosBusqueda(){
    debugger
    let titulo = document.querySelector("#busqueda").value
    console.log(titulo)
    navigate(`/?titulo=${titulo}`)
    debugger
    obtenerJuegosFiltros(titulo).then(datos => {
      limpiarSeccion()
      let section = document.querySelector(".seccion-principal");
      for(var categoria in datos){
        console.log(categoria)
        console.log(datos.categoria)
        let articuloCategoria = document.createElement("article")
        articuloCategoria.className = "article-categoria"
        let tituloCategoria = document.createElement("p")
        tituloCategoria.textContent = categoria
        let barra = document.createElement("hr")
        articuloCategoria.appendChild(tituloCategoria)
        articuloCategoria.appendChild(barra)
        section.appendChild(articuloCategoria)
        for(var juego in datos[categoria]){
          let objeto = datos[categoria].at(juego)
          let articuloJuego = document.createElement("article")
          articuloJuego.className = "article-juegos"
          let titulo = document.createElement("p")
          titulo.textContent = objeto.nombre;
          let enlace = document.createElement("a")
          enlace.href = `/juego?titulo=${objeto.nombre}`
          let contenedor = document.createElement("div");
          contenedor.className = "juego";
          let imagen = document.createElement("img");
          imagen.alt = "fondo-juego"
          imagen.src = objeto.fondoIcono;
          contenedor.appendChild(imagen)
          contenedor.appendChild(titulo)
          enlace.appendChild(contenedor)
          articuloJuego.appendChild(enlace)
          section.appendChild(articuloJuego)
        }
      }
    })
  }

  if(parametros.size == 0){
    debugger
    console.log(window.location.pathname)
    const juegos = obtenerJuegos().then(datos => {
      limpiarSeccion()
      let section = document.querySelector(".seccion-principal");
      for(var categoria in datos){
        console.log(categoria)
        console.log(datos.categoria)
        let articuloCategoria = document.createElement("article")
        articuloCategoria.className = "article-categoria"
        let tituloCategoria = document.createElement("p")
        tituloCategoria.textContent = categoria
        let barra = document.createElement("hr")
        articuloCategoria.appendChild(tituloCategoria)
        articuloCategoria.appendChild(barra)
        section.appendChild(articuloCategoria)
        for(var juego in datos[categoria]){
          let objeto = datos[categoria].at(juego)
          let articuloJuego = document.createElement("article")
          articuloJuego.className = "article-juegos"
          let titulo = document.createElement("p")
          titulo.textContent = objeto.nombre;
          let enlace = document.createElement("a")
          enlace.href = `/juego?titulo=${objeto.nombre}`
          let contenedor = document.createElement("div");
          contenedor.className = "juego";
          let imagen = document.createElement("img");
          imagen.alt = "fondo-juego"
          imagen.src = objeto.fondoIcono;
          contenedor.appendChild(imagen)
          contenedor.appendChild(titulo)
          enlace.appendChild(contenedor)
          articuloJuego.appendChild(enlace)
          section.appendChild(articuloJuego)
        }
      }
    })
  }

  return (
    <div>
      <HeaderComponent />

      <section className="seccion-principal">
        <article className="article-barra-busqueda">
          <BarraBusqueda placeholder={"Buscar juego..."} funcion={obtenerJuegosBusqueda} />
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default Inicio;
