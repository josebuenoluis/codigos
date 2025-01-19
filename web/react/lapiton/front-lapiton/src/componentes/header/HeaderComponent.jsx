import React from 'react'
import { Link } from 'react-router-dom'
import { useState } from 'react'
import Logo from '../../assets/imagenLogoPiton.png'
import '../css/HeaderComponent.css'

function HeaderComponent() {

  const [categorias,SetCategorias] = useState(["Accion","Multijugador","Supervivencia"]);
  const [menuDesplegado,SetmenuDesplegado] = useState(false);
  const [mouseMenu,SetMouseMenu] = useState(false);
  const [mouseCategoria,SetMouseCategoria] = useState(false);

  function desplegableCategorias(e){
    let lista = document.getElementById("desplegable-categorias");  
    let elemento = "";
    if(!menuDesplegado){
      for(var categoria in categorias){
        elemento = document.createElement("li");
        elemento.textContent = categorias.at(categoria);  
        elemento.onMouseMove = desplegableCategorias;
        lista.appendChild(elemento);
      }
      SetmenuDesplegado(true);
    }
  }

  function cerrarMenu(e){
      let lista = document.getElementById("desplegable-categorias");
      for(var i = 0;i < lista.childElementCount+2;i++){
        lista.removeChild(lista.childNodes.item(0));
      SetmenuDesplegado(false);
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
            <li><Link className='enlace' to="/">Inicio</Link></li>
            <li>
              <a href="#" className='enlace' onMouseMove={desplegableCategorias}>Categorias</a>
              <ul id='desplegable-categorias' onMouseMove={desplegableCategorias} onMouseLeave={cerrarMenu}>   
              </ul>
            </li>
            <li><Link className='enlace' to="ranking">Ranking</Link></li>
            <li><Link className='enlace' to="novedades">Novedades</Link></li>
          <li>
            <Link to="registro">
              <svg id="user-icono" width="76" height="73" viewBox="0 0 76 73" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M75.5 37.5C75.5 56.7985 58.7433 72.5 38 72.5C17.2567 72.5 0.5 56.7985 0.5 37.5C0.5 18.2015 17.2567 2.5 38 2.5C58.7433 2.5 75.5 18.2015 75.5 37.5Z" fill="white" stroke="black"/>
                <path d="M38.5002 11.8333C41.6386 11.8333 44.6484 13.0801 46.8676 15.2992C49.0868 17.5184 50.3335 20.5283 50.3335 23.6667C50.3335 26.8051 49.0868 29.8149 46.8676 32.0341C44.6484 34.2533 41.6386 35.5 38.5002 35.5C35.3618 35.5 32.3519 34.2533 30.1327 32.0341C27.9136 29.8149 26.6668 26.8051 26.6668 23.6667C26.6668 20.5283 27.9136 17.5184 30.1327 15.2992C32.3519 13.0801 35.3618 11.8333 38.5002 11.8333ZM38.5002 41.4167C51.576 41.4167 62.1668 46.7121 62.1668 53.25V59.1667H14.8335V53.25C14.8335 46.7121 25.4243 41.4167 38.5002 41.4167Z" fill="black"/>
              </svg>
            </Link>
          </li>
          </ul>
        </nav>
    </header>
  )
}

export default HeaderComponent;