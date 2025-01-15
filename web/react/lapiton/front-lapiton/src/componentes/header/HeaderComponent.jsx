import React from 'react'
import { Link } from 'react-router-dom'
import Logo from '../../assets/imagenLogoPiton.png'
import '../css/HeaderComponent.css'

function HeaderComponent() {
  return (
    <header>
        <div className="logo-header">
            <p>laPiton</p>
            <img src={Logo} alt="logo" />
        </div>
        <nav>
            <Link to="/">Inicio</Link>
            <a href="#">Categorias</a>
            <Link to="ranking">Ranking</Link>
            <Link to="novedades">Novedades</Link>
        </nav>
    </header>
  )
}

export default HeaderComponent;