import React,{useContext} from 'react'
import { Link } from 'react-router-dom'
import { useState } from 'react'
import Logo from '../../assets/logo-piton.svg'
import UserIcon from '../../assets/user-icon.svg'
import '../css/HeaderComponent.css'
import { userContext } from '../../context/userContext'
import { useNavigate } from "react-router-dom";

function HeaderComponent() {

  const navigate = useNavigate();

  const {user,setLocalStorage} = useContext(userContext)
  const [categorias,SetCategorias] = useState(["Acción","Multijugador","Supervivencia"]);
  const [menuDesplegado,SetmenuDesplegado] = useState(false);

  function cerrarSesion(){
    if(user.nombre != ""){
      window.localStorage.setItem("user",JSON.stringify({"nombre":"","avatar":"src/assets/user-icon.svg","tiempo":0}))
      location.reload()
    }
  }

  function desplegableCategorias(e){
    let lista = document.getElementById("desplegable-categorias");  
    let seccion = document.querySelector("section");
    let elemento = "";
    if(!menuDesplegado){
      for(var categoria in categorias){
        elemento = document.createElement("li");
        elemento.textContent = categorias.at(categoria);  
        elemento.onMouseMove = desplegableCategorias;
        lista.appendChild(elemento);
      }
    } 
    seccion.style.contain = "none";
    SetmenuDesplegado(true); 
  }

  function cerrarMenu(e){
    let lista = document.getElementById("desplegable-categorias");
    let seccion = document.querySelector("section");
    for(var i = 0;i < lista.childElementCount+2;i++){
      lista.removeChild(lista.childNodes.item(0));
    SetmenuDesplegado(false);
    seccion.style.contain = "content";
    }
  }

  async function obtenerCategoria(categoria){
    try{
      const peticion = {
        method: "GET",
      };
      const response = await fetch(`http://lapiton.zapto.org:5000/?categoria=${categoria}`,peticion)

      if (response.ok) {
        console.log("Exito");
        const datos = await response.json();
        return datos;
      }
    } catch (error) {
      console.log(error);
      return null;
    }
  }

  function limpiarSeccion(){
    let section = document.querySelector(".seccion-principal");
    let articleJuegos = section.querySelectorAll(".article-juegos");
    articleJuegos.forEach((juego) => {
      section.removeChild(juego);
    });
    let articleCategorias = section.querySelectorAll(".article-categoria");
    articleCategorias.forEach((categoria) => {
        section.removeChild(categoria);
      });
  }

  function obtenerJuegosCategoria(e){
    debugger
    let categoria = e.target.textContent
    navigate(`/?categoria=${categoria}`)
      limpiarSeccion()
      const juegos = obtenerCategoria(categoria).then(datos => {
        let section = document.querySelector(".seccion-principal");
        debugger
        for(var categoria in datos){
        debugger
        console.log(categoria)
        console.log(datos.categoria)
        let articuloCategoria = document.createElement("article")
        articuloCategoria.className = "article-categoria"
        let tituloCategoria = document.createElement("p")
        tituloCategoria.textContent = categoria
        let barra = document.createElement("hr")
        articuloCategoria.appendChild(tituloCategoria)
        articuloCategoria.appendChild(barra)
        section.appendChild(articuloCategoria)
        for(var juego in datos[categoria]){
          let objeto = datos[categoria].at(juego)
          let articuloJuego = document.createElement("article")
          articuloJuego.className = "article-juegos"
          let enlace = document.createElement("a")
          enlace.href = "/juego"
          let contenedor = document.createElement("div");
          contenedor.className = "juego";
          let imagen = document.createElement("img");
          imagen.alt = "fondo-juego"
          imagen.src = objeto.fondoIcono;
          let titulo = document.createElement("p")
          titulo.textContent = objeto.nombre;
          contenedor.appendChild(imagen)
          contenedor.appendChild(titulo)
          enlace.appendChild(contenedor)
          articuloJuego.appendChild(enlace)
          section.appendChild(articuloJuego)
        }
      }
    })
  }
  
  return (
    <header>
        <div className="logo-header">
            <img src={Logo} alt="logo" />
        </div>
        <nav>
          <ul>
            <li><Link className='enlace' to="/">Inicio</Link></li>
            <li onMouseMove={desplegableCategorias} onMouseLeave={cerrarMenu} onClick={obtenerJuegosCategoria}>
              <a href="#" className='enlace' id='enlace-categorias' >Categorias</a>
              <ul id='desplegable-categorias'>   
              </ul>
            </li>
            <li><Link className='enlace' to="/ranking">Ranking</Link></li>
            <li><Link className='enlace' to="/novedades">Novedades</Link></li>
          <li>
            <Link to="/login">
              <img src={user.avatar} id='user-icono' alt="" onChange={e => setLocalStorage({"nombre":user.nombre,"avatar":user.avatar,"tiempo":user.tiempo})} />
            </Link>
          </li>
          <li>
            <img src={"src/assets/deslog.svg"} id='deslog-icono' alt="icono-deslog" onClick={cerrarSesion} />
          </li>
          </ul>
        </nav>
    </header>
  )
}

export default HeaderComponent;