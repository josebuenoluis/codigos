import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import InicioComponent from './components/InicioComponent'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <InicioComponent />
    </>
  )
}

export default App
