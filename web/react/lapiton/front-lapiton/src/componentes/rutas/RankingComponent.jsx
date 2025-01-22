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
  function obtenerCategorias(){

  }

  // Para añadir las categorias al elemento Select
  function listarCategorias(){

  }

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
          <table>
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