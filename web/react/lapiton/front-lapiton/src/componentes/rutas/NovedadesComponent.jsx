import React from "react";
import { Link } from "react-router-dom";
import HeaderComponent from "../header/HeaderComponent";
import FooterComponent from "../footer/FooterComponent";
import DesplegableComponent from "../utils/DesplegableComponent";
import BarraBusqueda from "../utils/BarraBusqueda";

function Novedades() {
  return (
    <div>
      <HeaderComponent />
      <section>
      <article className="article-categoria">
             <p>Novedades</p>
             <hr />
        </article>
        <article className="article-contenido">
          
        </article>
      </section>
      <FooterComponent />
    </div>
  );
}

export default Novedades;
