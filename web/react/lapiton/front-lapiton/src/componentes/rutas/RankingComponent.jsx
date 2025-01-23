import React from 'react'
import { Link } from 'react-router-dom'
import HeaderComponent from '../header/HeaderComponent';
import FooterComponent from '../footer/FooterComponent';
import BarraBusqueda from '../utils/BarraBusqueda';
import DesplegableComponent from '../utils/DesplegableComponent';
import "../css/RankingComponent.css"
function RankingComponent() {




  // Para obtener los puntajes segun los filtros ingresados
  function obtenerPuntajes(){

  }

  // Para hacer una peticion sobre las categorias de los juegos
  async function obtenerCategorias(){
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

  const categorias = obtenerCategorias().then(datos =>{
    let desplegable = document.querySelector("#categoria-seleccionada")
    for(var categoria in datos){
      let opcion = document.createElement("option")
      let categoriaAñadir = datos.at(categoria)
      opcion.value = categoriaAñadir
      opcion.name = categoriaAñadir
      opcion.textContent = categoriaAñadir
      desplegable.appendChild(opcion)
    }
  })
  return (
    <div>
      <HeaderComponent />
      <section>
        <article className='article-filtros'>
          <DesplegableComponent />
          <BarraBusqueda />
        </article>
        <article className="article-titulo-ranking">
          <p>Ranking de jugadores</p>
          <hr />
        </article>
        <article className='article-tabla'>
          <table cellSpacing={0} cellPadding={0}>
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