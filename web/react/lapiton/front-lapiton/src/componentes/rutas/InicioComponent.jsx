import React,{useContext} from "react";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import "../css/InicioComponent.css";
import FondoTiburon from "../../assets/fondoTiburonInicio.svg"
import FondoSerpiente from "../../assets/campo-serpiente-1 1.svg"
import FondoBestia from "../../assets/campo-bestia-1 1.svg"
import { Link } from "react-router-dom";
import { userContext } from "../../context/userContext";

function Inicio() {
<<<<<<< HEAD
  const peticionLog = async() =>{
    try {
      const peticion = {
        method: "GET",
      };
      const response = await fetch(
        "http://127.0.0.1:5000/",
        peticion
      );

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
  // const userLog = () =>{
  //   peticionLog().then(datos =>{
  //     if(datos.avatar!=""||datos!=null){
  //       document.querySelector("#user-icono").src = datos.avatar
  //     }
  //   })
  // }
  // userLog()
=======
  
  const {user,setUser} = useContext(userContext)
  
>>>>>>> af5701ca91593d76b9185f4af78acd71b916146a
  return (
    <div>
      <HeaderComponent />

      <section>
        <article className="article-barra-busqueda">
          <div className="barra-busqueda">
            <input type="text" id="busqueda" placeholder="Buscar..." />
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                x="0px"
                y="0px"
                viewBox="0 0 50 50"
              >
                <path d="M 21 3 C 11.601563 3 4 10.601563 4 20 C 4 29.398438 11.601563 37 21 37 C 24.355469 37 27.460938 36.015625 30.09375 34.34375 L 42.375 46.625 L 46.625 42.375 L 34.5 30.28125 C 36.679688 27.421875 38 23.878906 38 20 C 38 10.601563 30.398438 3 21 3 Z M 21 7 C 28.199219 7 34 12.800781 34 20 C 34 27.199219 28.199219 33 21 33 C 13.800781 33 8 27.199219 8 20 C 8 12.800781 13.800781 7 21 7 Z"></path>
              </svg>
            </button>
          </div>
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
        <article className="article-juegos">
          <Link to="/juego">
            <div className="juego">
              <img src={FondoSerpiente} alt="fondo-juego" />
              <p>La Serpiente</p>
            </div>
          </Link>
        </article>
        <article className="article-juegos">
          <Link to="/juego">
            <div className="juego">
              <img src={FondoBestia} alt="fondo-juego" />
              <p>La Bestia</p>
            </div>
          </Link>
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default Inicio;
