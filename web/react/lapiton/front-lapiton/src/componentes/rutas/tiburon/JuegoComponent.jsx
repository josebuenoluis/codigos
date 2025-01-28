import React, { useEffect,useContext } from "react";
import HeaderComponent from "../../header/HeaderComponent";
import FooterComponent from "../../footer/FooterComponent";
import "../../css/JuegoComponent.css";
import { userContext } from "../../../context/userContext";
function JuegoComponent() {
  
  const {user,setLocalStorage} = useContext(userContext)

 useEffect(() =>{
  setTimeout(() =>{
    let script = document.createElement("script")
    script.src = "http://localhost:5173/src/componentes/rutas/tiburon/tiburon.js "
    document.body.appendChild(script)
    window.localStorage.setItem("puntaje",JSON.stringify({"nombre":user.nombre,"puntaje":0,"dificultad":0,"categoria":"supervivencia","juego":"El Tiburon"}))
  },[])
 })

    // Para hacer una peticion sobre que devolvera las categorias de juegos y puntos y informacion de los usuarios
    async function obtenerRanking(){
      try{
        const peticion = {
          method: "GET",
        };
        const response = await fetch("http://10.102.9.204:5000/ranking",peticion)
  
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
  
    const ranking = obtenerRanking().then(datos =>{
      let tablaJugadores = document.querySelector("#tabla-ranking")
      for(var jugador in datos.jugadores){
        let jugadorAgregar = datos.jugadores.at(jugador)
        let fila = document.createElement("tr")
        let columnaNombre = document.createElement("td")
        columnaNombre.textContent = jugadorAgregar.nombre
        fila.appendChild(columnaNombre)
        let columnaPuntaje = document.createElement("td")
        columnaPuntaje.textContent = jugadorAgregar.puntaje
        fila.appendChild(columnaPuntaje)
        let columnaDificultad = document.createElement("td")
        columnaDificultad.textContent = jugadorAgregar.dificultad
        fila.appendChild(columnaDificultad)
        tablaJugadores.appendChild(fila)
      }
    }
  )
 
  return (
    <div className="main">
      <HeaderComponent />
      <section>
        <article className="article-categoria">
          <p>El tiburon</p>
          <hr />
        </article>
        <article className="article-juego">
          <table id="tabla-ranking">
            <tr>
              <th colSpan="3">TOP 10</th>
            </tr>
            <tr>
              <th>Nombre</th>
              <th>Puntos</th>
              <th>Dificultad</th>
            </tr>
          </table>
          <div class="puntaje">
            <p id="tituloPuntos">PUNTOS:</p>
            <p id="puntos"></p>
            <p id="tituloDificultad">DIFICULTAD:</p>
            <p id="dificultad"></p>
          </div>
          <div class="campo"></div>
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default JuegoComponent;
