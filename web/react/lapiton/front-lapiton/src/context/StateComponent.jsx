import React, { useState } from 'react'
import { userContext } from './userContext'

function StateComponent({children}) {

    const [user,setUser] = useState({"nombre":"","avatar":"src/assets/user-icon.svg"})

    const loginUsuario = (usuario) =>{
        setUser(usuario)
    }

  return (
    <userContext.Provider
    value={{user,setUser,loginUsuario}}>
        { children }
    </userContext.Provider>
  )
}

export default StateComponent