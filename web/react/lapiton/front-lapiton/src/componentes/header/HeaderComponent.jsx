import React from 'react'
import { Link } from 'react-router-dom'
import { useState } from 'react'
import Logo from '../../assets/imagenLogoPiton.png'
import '../css/HeaderComponent.css'

function HeaderComponent() {

  const [categorias,SetCategorias] = useState(["Accion","Multijugador","Supervivencia"]);

  function desplegableCategorias(){
    let lista = document.getElementById("#desplegable-categorias");
    for(categoria in categorias){
      lista.appendChild();
    }
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
              <a href="#">Categorias</a>
              <ul id='desplegable-categorias' onMouseMove={desplegableCategorias}>
                    
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