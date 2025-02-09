import React,{useContext} from "react";
import { useLocation } from "react-router-dom";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import "../css/InicioComponent.css";
import { userContext } from "../../context/userContext";
import BarraBusqueda from "../utils/BarraBusqueda";
import { useNavigate } from "react-router-dom";

function Inicio() {
  
  // Creamos un objeto navegador
  const navigate = useNavigate();
  
  const {user,setUser} = useContext(userContext)
  const location = useLocation()
  // Creamos un objeto para obtener los valores del enrutado
  // que hemos recibido
  const parametros = new URLSearchParams(location.search)
  

  // Funcion para obtener los juegos disponibles
  // mediante una peticion GET a la API de Flask
 async function obtenerJuegos(){
    try{
      const peticion = {
        method: "GET",
      };
      const response = await fetch("http://lapiton.zapto.org:5000/",peticion)

      if (response.ok) {
        console.log("Exito");
        // Obtenemos los datos en formato JSON esperando al
        // objeto response asincrono
        const datos = await response.json();
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  // Funcion para obtener los juegos por su titulo, mediante
  // una peticion GET a la API
  async function obtenerJuegosFiltros(titulo){
    try{
      const peticion = {
        method: "GET",
      };
      const response = await fetch(`http://lapiton.zapto.org:5000/?titulo=${titulo}`,peticion)
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

  // Funcion para limpiar la lista de juegos, que usaremos
  // para mostrar solo los juegos segun los filtros
  function limpiarSeccion(){
    let section = document.querySelector(".seccion-principal");
    let articleJuegos = section.querySelectorAll(".article-juegos");
    // Obtenemos todos los article-juegos dentro de la Section
    articleJuegos.forEach((juego) => {
      section.removeChild(juego);
    });
    // Obtenemos todos los article-categoria dentro de la Section
    let articleCategorias = section.querySelectorAll(".article-categoria");
    articleCategorias.forEach((categoria) => {
        section.removeChild(categoria);
      });
  }

  // Funcion para obtener los juegos segun el titulo a buscar
  // por el usuario
  function obtenerJuegosBusqueda(){
    let titulo = document.querySelector("#busqueda").value
    console.log(titulo)
    navigate(`/?titulo=${titulo}`)
    obtenerJuegosFiltros(titulo).then(datos => {
      // Luego de obtener los juegos, limpiamos toda la section
      limpiarSeccion()
      let section = document.querySelector(".seccion-principal");
      for(var categoria in datos){
        // Creamos un article por cada categoria para añadirla a la Section
        let articuloCategoria = document.createElement("article")
        articuloCategoria.className = "article-categoria"
        let tituloCategoria = document.createElement("p")
        tituloCategoria.textContent = categoria
        let barra = document.createElement("hr")
        articuloCategoria.appendChild(tituloCategoria)
        articuloCategoria.appendChild(barra)
        section.appendChild(articuloCategoria)
        // Luego de crear la categoria de juego, empezaremos
        // a crear los contenedores de los juegos para añadirlos
        // a su respectiva categoria
        for(var juego in datos[categoria]){
          // Obtenemos cada juego por su posicion en los valores
          // de la lista de juegos de cada categoria en el JSON
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

  // Si no se le pasa ningun parametro para obtener un juego por su
  // titulo, simplemente se mostraran todos los juegos de todas
  // las categorias
  if(parametros.size == 0){
    const juegos = obtenerJuegos().then(datos => {
      limpiarSeccion()
      let section = document.querySelector(".seccion-principal");
      for(var categoria in datos){
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
