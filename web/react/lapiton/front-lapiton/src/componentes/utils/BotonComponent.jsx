import React from 'react'
import "../css/BotonRegistroComponent.css"

function BotonComponent(props) {
    return (
        <input type="button" onClick={props.funcion} value={props.value} id={props.id} className={props.className} />
      )
}

export default BotonComponent
