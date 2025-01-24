import React, { useEffect } from "react";
import HeaderComponent from "../../header/HeaderComponent";
import FooterComponent from "../../footer/FooterComponent";
import "../../css/JuegoComponent.css";

function JuegoComponent() {
  

 useEffect(() =>{
  setTimeout(() =>{
    let script = document.createElement("script")
    script.src = "http://localhost:5173/src/componentes/rutas/tiburon/tiburon.js "
    document.body.appendChild(script)
  },[])
 })

 
  return (
    <div className="main">
      <HeaderComponent />
      <section>
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
            <tr>
              <td>Jose</td>
              <td>10</td>
              <td>20</td>
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
      </section>
      <FooterComponent />
    </div>
  );
}

export default JuegoComponent;
