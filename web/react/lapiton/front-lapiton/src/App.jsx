import { useState } from 'react'
import { Routes,Route } from 'react-router-dom'
import './App.css'
import Inicio from './componentes/rutas/InicioComponent'
import NovedadesComponent from './componentes/rutas/NovedadesComponent'
import RankingComponent from './componentes/rutas/RankingComponent'
import JuegoComponent from './componentes/rutas/tiburon/JuegoComponent'
import './componentes/css/fonts.css'
import RegistroComponent from './componentes/rutas/RegistroComponent'
import LoginComponent from './componentes/rutas/LoginComponent'
import StateComponent from './context/StateComponent'
import VentanaAgregarComponent from './componentes/rutas/VentanaAgregarComponent'
import NovedadComponent from './componentes/rutas/NovedadComponent'

function App() {
  return (
    <>
    <StateComponent>
      <div className="Aplicacion">
        <Routes>
          <Route path="/" element={ <Inicio  /> } />
          <Route path="novedades" element={ <NovedadesComponent /> } />
          <Route path="ranking" element={ <RankingComponent /> } />
          <Route path="juego" element={ <JuegoComponent /> } />
          <Route path="registro" element={<RegistroComponent />} />
          <Route path="login" element={<LoginComponent />} />
          <Route path="agregar" element={<VentanaAgregarComponent />} />
          <Route path="novedades/novedad" element={<NovedadComponent />} />
          
        </Routes>
      </div>
    </StateComponent>
    </>
  )
}

export default App
