import React from 'react'
import "../css/VentanaAgregarComponent.css"
import imagenInsertar from "../../assets/inserteImagen.png"
import HeaderComponent from '../header/HeaderComponent'
import FooterComponent from '../footer/FooterComponent'
import InputTextComponent from '../utils/InputTextComponent'
import BotonComponent from '../utils/BotonComponent'
import DescripcionComponent from '../utils/DescripcionComponent'
import SelectorArchivos from '../utils/SelectorArchivosComponent'

function VentanaAgregarComponent() {

    function obtenerImagen(e){
        let img = document.querySelector("#img-novedad");
        let file = document.querySelector("#id-selector");
        debugger
        if(e.target.files[0]){
            const reader = new FileReader()
            reader.onload = function(e){
                console.log(e.result)
                img.src = e.target.result
            }
            let base = e.target.files[0]
            console.log(base)
            reader.readAsDataURL(e.target.files[0])
        }else{
            img.src = imagenInsertar
        }
    }

    function obtenerNovedad(){
        let titulo = document.querySelector("#titulo").value
        let img = document.querySelector("#img-novedad").src;
        let descripcion = document.querySelector("#descripcion").value
        let novedad = {"titulo":titulo,"imagen":img,"descripcion":descripcion}
        return novedad
    }

    async function subirNovedad(){
        let novedad = obtenerNovedad()
        try {
          const response = await fetch("http://127.0.0.1:5000/novedades/agregar", {
            // Definimos el metodo que vamos a utilizar GET,POST,PUT,DELETE,etc...
            method: "POST",
            //Definimos un headers que sera el tipo de dato que vamos a enviar
            headers: { "Content-Type": "application/json" },
            //Agregamos el contenido que vamos a enviar
            body: JSON.stringify(novedad),
          });
          if (response.ok) {
            let jsonResponse = JSON.stringify(novedad);
            console.log(jsonResponse);
          }
        } catch (error) {
          console.log(error);
        }
      }

  return (
    <div>
        <HeaderComponent />
        <section>
          <article className="article-titulo-agregar">
            <p>Agregar novedad</p>
            <hr />
          </article>
          <article className="article-agregar">
            <div className="panel-agregar">
                <div className="icono-imagen">
                    <img id="img-novedad" src={imagenInsertar} alt="Imagen Novedad" />
                </div>
                <SelectorArchivos id={"id-selector"} funcion={obtenerImagen} className={"selector-archivos"} />
                <InputTextComponent
                type={"text"}
                id={"titulo"}
                className={"text-component"}
                placeholder={"Titulo de novedad..."}
              />
                <DescripcionComponent placeholder={"Ingrese una descripción..."}
                 id={"descripcion"} />
                <BotonComponent
                id={"subir-novedad"}
                value={"Subir novedad"}
                className={"boton-component"}
                funcion={subirNovedad} />
            </div>
          </article>
        </section>
        <FooterComponent />
    </div>
  )
}

export default VentanaAgregarComponent