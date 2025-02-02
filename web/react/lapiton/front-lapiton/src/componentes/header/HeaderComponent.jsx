import React,{useContext} from 'react'
import { Link } from 'react-router-dom'
import { useState } from 'react'
import Logo from '../../assets/logo-piton.svg'
import UserIcon from '../../assets/user-icon.svg'
import '../css/HeaderComponent.css'
import { userContext } from '../../context/userContext'

function HeaderComponent() {

  const {user,setLocalStorage} = useContext(userContext)

  const [categorias,SetCategorias] = useState(["Accion","Multijugador","Supervivencia"]);
  const [menuDesplegado,SetmenuDesplegado] = useState(false);

  function cerrarSesion(){
    if(user.nombre != ""){
      window.localStorage.setItem("user",JSON.stringify({"nombre":"","avatar":"src/assets/user-icon.svg","tiempo":0}))
      location.reload()
    }
  }

  function desplegableCategorias(e){
    let lista = document.getElementById("desplegable-categorias");  
    let elemento = "";
    debugger
    if(!menuDesplegado){
      for(var categoria in categorias){
        elemento = document.createElement("li");
        elemento.textContent = categorias.at(categoria);  
        elemento.onMouseMove = desplegableCategorias;
        lista.appendChild(elemento);
      }
    } 
    SetmenuDesplegado(true); 
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
            <img src={Logo} alt="logo" />
        </div>
        <nav>
          <ul>
            <li><Link className='enlace' to="/">Inicio</Link></li>
            <li onMouseMove={desplegableCategorias} onMouseLeave={cerrarMenu}>
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