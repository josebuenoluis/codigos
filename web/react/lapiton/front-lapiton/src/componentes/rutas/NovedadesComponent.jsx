import React from 'react'
import { Link } from 'react-router-dom'
import HeaderComponent from '../header/HeaderComponent';
import FooterComponent from '../footer/FooterComponent';
function Novedades() {
  return (
    <div>
        <h1>Pagina de novedades</h1>
        <Link to="/">Ir a inicio</Link>
    </div>
  )
}

export default Novedades;