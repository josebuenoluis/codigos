import React,{useContext} from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import "../css/InicioComponent.css";
import FondoTiburon from "../../assets/fondoTiburonInicio.svg"
import FondoSerpiente from "../../assets/campo-serpiente-1 1.svg"
import FondoBestia from "../../assets/campo-bestia-1 1.svg"
import { Link } from "react-router-dom";
import { userContext } from "../../context/userContext";
import BarraBusqueda from "../utils/BarraBusqueda";

function Inicio() {
  
  const {user,setUser} = useContext(userContext)
  console.log("Desde el inicio ",user.avatar)
  let listaJuegos = [];
  
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

  const juegos = obtenerJuegos().then(datos => {
    let section = document.querySelector(".seccion-principal");
    debugger
    for(var juego in datos){
      debugger
      let articuloJuego = document.createElement("article")
      articuloJuego.className = "article-juegos"
      let enlace = document.createElement("a")
      enlace.href = "/juego"
      let objeto = datos.at(juego)
      let contenedor = document.createElement("div");
      contenedor.className = "juego";
      let imagen = document.createElement("img");
      imagen.alt = "fondo-juego"
      imagen.src = objeto.fondoIcono;
      let titulo = document.createElement("p")
      titulo.textContent = objeto.nombre;
      contenedor.appendChild(imagen)
      contenedor.appendChild(titulo)
      debugger
      enlace.appendChild(contenedor)
      articuloJuego.appendChild(enlace)
      section.appendChild(articuloJuego)
    }
  })

  return (
    <div>
      <HeaderComponent />

      <section className="seccion-principal">
        <article className="article-barra-busqueda">
          <BarraBusqueda />
        </article>
        <article className="article-categoria">
             <p>Supervivencia</p>
             <hr />
        </article>
        
        
      </section>
      <FooterComponent />
    </div>
  );
}

export default Inicio;
