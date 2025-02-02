import React, { useState } from 'react'
import { userContext } from './userContext'

function StateComponent({children}) {
  // 10 minutops


  const tiempoMaximo = 300000
  let tiempoActual = new Date().getTime()

  let objetoUsuario = JSON.parse(window.localStorage.getItem("user"))
  if(objetoUsuario==null){
    window.localStorage.setItem("user",JSON.stringify({"nombre":"","avatar":"src/assets/user-icon.svg","tiempo":0}))
  }
  let tiempoGuardado = objetoUsuario.tiempo;
  console.log(tiempoGuardado)
  if(tiempoActual-tiempoGuardado > tiempoMaximo && tiempoGuardado != 0){
    console.log("Deslogueando")
    window.localStorage.setItem("user",JSON.stringify({"nombre":"","avatar":"src/assets/user-icon.svg","tiempo":0}))
  }
    const setLocalStorage = value => {
      try{
        window.localStorage.setItem("user",JSON.stringify(value))
        loginUsuario(window.localStorage.getItem("user"))

        console.log(window.localStorage.getItem("user"))
      }catch(error){
        console.error(error)
      }
    }
    const [user,setUser] = useState(
      JSON.parse(window.localStorage.getItem("user"))
    )

    const [novedad,SetNovedad] = useState("");

    const [Vibrando,SetVibrando] = useState(false)

    const loginUsuario = (usuario) =>{

        setUser(JSON.parse(usuario))
    }

  return (
    <userContext.Provider
    value={{user,setUser,loginUsuario,setLocalStorage,novedad,SetNovedad,Vibrando,SetVibrando}}>
        { children }
    </userContext.Provider>
  )
}

export default StateComponent