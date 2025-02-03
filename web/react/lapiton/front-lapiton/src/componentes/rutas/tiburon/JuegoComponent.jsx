import React, { useEffect,useContext } from "react";
import HeaderComponent from "../../header/HeaderComponent";
import FooterComponent from "../../footer/FooterComponent";
import "../../css/JuegoComponent.css";
import { userContext } from "../../../context/userContext";
import { useLocation } from "react-router-dom";

function JuegoComponent() {
  const {user,setLocalStorage} = useContext(userContext)
  const location = useLocation()
  const parametros = new URLSearchParams(location.search)
  

 useEffect(() =>{
  setTimeout(() =>{
    let script = document.createElement("script")
    script.src = "src/componentes/rutas/tiburon/tiburon.js "
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
        const response = await fetch("http://lapiton.zapto.org:5000/ranking",peticion)
  
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
  
    async function obtenerJuegosRelacionados(titulo){
      try{
        const peticion = {
          method: "GET",
        };
        const response = await fetch(`http://lapiton.zapto.org:5000/juego/relacionados?titulo=${titulo}`,peticion)
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
  
    if(parametros.size == 1){
      const tituloJuego = parametros.get("titulo")
      const juegos = obtenerJuegosRelacionados(tituloJuego).then(datos => {
        let section = document.querySelector(".main");
        for(var categoria in datos){
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
    <div>
      <HeaderComponent />
      <section className="main">
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
        <article className="article-categoria">
          <p>Controles del Juego</p>
          <hr />
        </article>

        <article className="control">
          <img src="src/assets/cursores.svg" alt="Cursores" />
        </article>
        <article className="control">
          <img src="src/assets/space-bar.svg" alt="Barra de espacio" />
        </article>
        <article className="control">
          <img src="src/assets/pause.svg" alt="Barra de espacio" />
        </article>
        <article className="article-categoria">
          <p>Juego relacionados</p>
          <hr />
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default JuegoComponent;
