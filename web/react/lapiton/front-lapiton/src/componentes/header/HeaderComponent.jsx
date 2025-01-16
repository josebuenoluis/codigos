import React from 'react'
import { Link } from 'react-router-dom'
import { useState } from 'react'
import Logo from '../../assets/imagenLogoPiton.png'
import '../css/HeaderComponent.css'

function HeaderComponent() {
  function desplegableCategorias(){
    console.log("DENTRO")
  }
  return (
    <header>
        <div className="logo-header">
            <p>laPiton</p>
            <img src={Logo} alt="logo" />
        </div>
        <nav>
          <ul>
            <li><Link to="/">Inicio</Link></li>
            <li>
              <ul id='desplegable-categorias' onMouseMove={desplegableCategorias}>
                <li>Categorias</li>
                <li>Accion</li>
                <li>Multijugador</li>
                <li>Supervivencia</li>
              </ul>
            </li>
            <li><Link to="ranking">Ranking</Link></li>
            <li><Link to="novedades">Novedades</Link></li>
          </ul>
        </nav>
    </header>
  )
}

export default HeaderComponent;