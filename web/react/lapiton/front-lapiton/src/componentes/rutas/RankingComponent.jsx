import React from 'react'
import { Link } from 'react-router-dom'
import HeaderComponent from '../header/HeaderComponent';
import FooterComponent from '../footer/FooterComponent';
import BarraBusqueda from '../utils/BarraBusqueda';
import DesplegableComponent from '../utils/DesplegableComponent';
import "../css/RankingComponent.css"
function RankingComponent() {

  async function obtenerRankingFiltros(){
    try{
      const peticion = {
        method: "GET",
      };
      debugger
      let filtro_busqueda = document.querySelector("#busqueda").value
      let filtro_categoria = document.querySelector("#categoria-seleccionada").value
      debugger
      console.log(filtro_categoria)
      console.log(filtro_busqueda)
      let response = ""
      if(filtro_busqueda=="" && filtro_categoria!=""){
        response = await fetch(`http://127.0.0.1:5000/ranking?categoria=${filtro_categoria}`,peticion)
      }else if(filtro_busqueda!="" && filtro_categoria!=""){
        response = await fetch(`http://127.0.0.1:5000/ranking?categoria=${filtro_categoria}&busqueda=${filtro_busqueda}`,peticion)
      }else if(filtro_busqueda!="" && filtro_categoria==""){
        response = await fetch(`http://127.0.0.1:5000/ranking?busqueda=${filtro_busqueda}`,peticion)
      }else{
        response = await fetch("http://127.0.0.1:5000/ranking",peticion)
      }

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

  function limpiarTabla(){
    let tablaJugadores = document.querySelector("#tabla-jugadores")
    let filas = tablaJugadores.querySelectorAll(".jugador-ranking");
    filas.forEach((fila) => {
        tablaJugadores.removeChild(fila);
      });
  }

  function mostrarFiltrosCategoria(){
    debugger
      limpiarTabla( )
      obtenerRankingFiltros().then(datos =>{
      let tablaJugadores = document.querySelector("#tabla-jugadores")
      let contador = 0
      console.log(datos)
      for(var jugador in datos.jugadores){
        contador += 1
        let jugadorAgregar = datos.jugadores.at(jugador)
        let fila = document.createElement("tr")
        fila.className = "jugador-ranking"
        let columnaPosicion = document.createElement("td")
        columnaPosicion.textContent = contador
        fila.appendChild(columnaPosicion)
        let columnaPuntaje = document.createElement("td")
        columnaPuntaje.textContent = jugadorAgregar.puntaje
        fila.appendChild(columnaPuntaje)
        let columnaNombre = document.createElement("td")
        columnaNombre.textContent = jugadorAgregar.nombre
        fila.appendChild(columnaNombre)
        let columnaJuego = document.createElement("td")
        columnaJuego.textContent = jugadorAgregar.juego
        fila.appendChild(columnaJuego)
        let columnaCategoria = document.createElement("td")
        columnaCategoria.textContent = jugadorAgregar.categoria
        fila.appendChild(columnaCategoria)
        tablaJugadores.appendChild(fila)
      }
    })
  }

  // Para hacer una peticion sobre que devolvera las categorias de juegos y puntos y informacion de los usuarios
  async function obtenerRanking(){
    try{
      const peticion = {
        method: "GET",
      };
      const response = await fetch("http://127.0.0.1:5000/ranking",peticion)

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
    let desplegable = document.querySelector("#categoria-seleccionada")
    let tablaJugadores = document.querySelector("#tabla-jugadores")
    for(var categoria in datos.categorias){
      let opcion = document.createElement("option")
      let categoriaAñadir = datos.categorias.at(categoria)
      opcion.value = categoriaAñadir
      opcion.name = categoriaAñadir
      opcion.textContent = categoriaAñadir
      desplegable.appendChild(opcion)
    }
    let contador = 0
    for(var jugador in datos.jugadores){
      contador += 1
      let jugadorAgregar = datos.jugadores.at(jugador)
      let fila = document.createElement("tr")
      fila.className = "jugador-ranking"
      let columnaPosicion = document.createElement("td")
      columnaPosicion.textContent = contador
      fila.appendChild(columnaPosicion)
      let columnaPuntaje = document.createElement("td")
      columnaPuntaje.textContent = jugadorAgregar.puntaje
      fila.appendChild(columnaPuntaje)
      let columnaNombre = document.createElement("td")
      columnaNombre.textContent = jugadorAgregar.nombre
      fila.appendChild(columnaNombre)
      let columnaJuego = document.createElement("td")
      columnaJuego.textContent = jugadorAgregar.juego
      fila.appendChild(columnaJuego)
      let columnaCategoria = document.createElement("td")
      columnaCategoria.textContent = jugadorAgregar.categoria
      fila.appendChild(columnaCategoria)
      tablaJugadores.appendChild(fila)
    }
  }
)
  return (
    <div>
      <HeaderComponent />
      <section>
        <article className='article-filtros'>
          <DesplegableComponent funcion={mostrarFiltrosCategoria} />
          <BarraBusqueda funcion={mostrarFiltrosCategoria} />
        </article>
        <article className="article-titulo-ranking">
          <p>Ranking de jugadores</p>
          <hr />
        </article>
        <article className='article-tabla'>
          <table cellSpacing={0} cellPadding={0} id='tabla-jugadores'>
            <thead>
              <tr>
                <th>Posicion</th>
                <th>Puntaje</th>
                <th>Nombre</th>
                <th>Juego</th>
                <th>Categoria</th>
              </tr>
            </thead>

          </table>
        </article>
        </section>
      <FooterComponent />
    </div>
  )
}

export default RankingComponent;