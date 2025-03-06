import React from 'react'

function InicioComponent() {
  return (
    <div>
        <h2>Hola mundo!</h2>
        <form action="http://192.168.1.213:5000/subir" method='post'>
            <label htmlFor="nombre">Nombre: </label>
            <input type="text" name='nombre' id='nombre' />
            <input type="submit" id="upload" />
        </form>
    </div>
  )
}

export default InicioComponent