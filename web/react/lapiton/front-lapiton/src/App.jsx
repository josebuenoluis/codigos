import { useState } from 'react'
import { Routes,Route } from 'react-router-dom'
import './App.css'
import Inicio from './componentes/rutas/inicio'
import Novedades from './componentes/rutas/novedades'
import './componentes/css/fonts.css'

function App() {
  return (
    <>
      <div className="Aplicacion">
      <Routes>
        <Route path="/" element={ <Inicio /> } />
        <Route path="novedades" element={ <Novedades /> } />
      </Routes>
    </div>
    </>
  )
}

export default App
