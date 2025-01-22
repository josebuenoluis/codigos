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

  let listaJuegos = [];
  
 async function obtenerJuegos(){
    try{
      const peticion = {
        method: "GET",
      };
      debugger
      const response = fetch("http://127.0.0.1:5000/",peticion)

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

  const juegos = obtenerJuegos().then(datos => {
    let articuloJuego = document.querySelector(".article-juegos")
    for(var juego in datos){
      debugger
      let contenedor = document.createElement("div");
      let imagen = document.createElement("img");
      imagen.alt = "fondo-juego"
      imagen.src = juego.fondoIcono;
      let titulo = document.createElement("p")
      titulo.textContent = juego.nombre;
      articuloJuego.appendChild(contenedor)
      listaJuegos.push(contenedor)
    }
    console.log(listaJuegos)
  })

  return (
    <div>
      <HeaderComponent />

      <section>
        <article className="article-barra-busqueda">
          <BarraBusqueda />
        </article>
        <article className="article-categoria">
             <p>Supervivencia</p>
             <hr />
        </article>
        <article className="article-juegos">
          <Link to="/juego">
          <div className="juego">
            <img src={FondoTiburon} alt="fondo-juego" />
            <p>El tiburon</p>
          </div>
          </Link>
          
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default Inicio;
