<<<<<<< HEAD
import React from 'react'
import { Link } from 'react-router-dom'
import HeaderComponent from '../header/HeaderComponent'

function Inicio() {
  return (
    <div>
        <HeaderComponent />
    </div>
  )
}

export default Inicio
=======
import { Link } from "react-router-dom";
import novedades from "./novedades";
function Inicio() {
    return (
      <div>
        <h1>Esta es la página de inicio</h1>
        <Link to={novedades}>Haga click para novedades</Link>
      </div>
    );
  }
  
  export default Inicio;
>>>>>>> f8786adc25c786d6dcbf9a20e162a6d2f487977c
