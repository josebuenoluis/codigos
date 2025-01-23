import React,{useContext} from 'react'
import { Link } from 'react-router-dom'
import { useState } from 'react'
import Logo from '../../assets/imagenLogoPiton.png'
import UserIcon from '../../assets/user-icon.svg'
import '../css/HeaderComponent.css'
import { userContext } from '../../context/userContext'

function HeaderComponent() {

  const {user,setLocalStorage} = useContext(userContext)

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
            <li><Link className='enlace' to="/ranking">Ranking</Link></li>
            <li><Link className='enlace' to="/novedades">Novedades</Link></li>
          <li>
            <Link to="/login">
              <img src={user.avatar} id='user-icono' alt="" onChange={e => setLocalStorage({"nombre":user.nombre,"avatar":user.avatar,"tiempo":user.tiempo})} />
            </Link>
          </li>
          </ul>
        </nav>
    </header>
  )
}

export default HeaderComponent;