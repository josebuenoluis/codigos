import React, { useState } from 'react'
import { userContext } from './userContext'

function StateComponent({children}) {
  
  // Definimos el tiempo maximo sesion para el usuario
  const tiempoMaximo = 300000
  // Obtenemos el tiempo actual del usuario para luego comparar
  let tiempoActual = new Date().getTime()

  // Obtenemos el usuario guardado en localStorage si existe
  let objetoUsuario = JSON.parse(window.localStorage.getItem("user"))
  if(objetoUsuario==null){
    // Si no hay usuario logueado en localStorage, simplemente lo guardamos como vacio
    window.localStorage.setItem("user",JSON.stringify({"nombre":"","avatar":"src/assets/user-icon.svg","tiempo":0}))
  }

  // Obtenemos el tiempo guardado del usuario al loguearse
  let tiempoGuardado = objetoUsuario.tiempo;

  // Comparamos el timpo guardado del usuario al loguearse, con el 
  // tiempo actual y con el tiempo maximo de sesion
  if(tiempoActual-tiempoGuardado > tiempoMaximo && tiempoGuardado != 0){
    // Si el usuario supera el tiempo de sesion la cerramos
    window.localStorage.setItem("user",JSON.stringify({"nombre":"","avatar":"src/assets/user-icon.svg","tiempo":0}))
  }

  // Funcion para guardar el usuario  en localStorage
    const setLocalStorage = value => {
      try{
        window.localStorage.setItem("user",JSON.stringify(value))
        loginUsuario(window.localStorage.getItem("user"))

      }catch(error){
        console.error(error)
      }
    }

    // Definimos el contexto del usuario mediante el usuario guardado en
    // localStorage
    const [user,setUser] = useState(
      JSON.parse(window.localStorage.getItem("user"))
    )

    const [novedad,SetNovedad] = useState("");

    const [Vibrando,SetVibrando] = useState(false)

    // FUncion para guardar el usuario guardado en el contexto
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