import { useState } from 'react'
import { Routes,Route } from 'react-router-dom'
import './App.css'
import Inicio from './componentes/rutas/InicioComponent'
import Novedades from './componentes/rutas/novedades'
import Ranking from './componentes/rutas/ranking'
import JuegoComponent from './componentes/rutas/tiburon/JuegoComponent'
import './componentes/css/fonts.css'
import RegistroComponent from './componentes/rutas/RegistroComponent'
import LoginComponent from './componentes/rutas/LoginComponent'

function App() {
  return (
    <>
      <div className="Aplicacion">
      <Routes>
        <Route path="/" element={ <Inicio /> } />
        <Route path="novedades" element={ <Novedades /> } />
        <Route path="ranking" element={ <Ranking /> } />
        <Route path="juego" element={ <JuegoComponent /> } />
        <Route path="registro" element={<RegistroComponent />} />
        <Route path="login" element={<LoginComponent />} />

      </Routes>
    </div>
    </>
  )
}

export default App
