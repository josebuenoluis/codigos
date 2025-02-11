import React from 'react'
import "../css/BotonAgregarComponent.css"

function BotonAgregar(props) {
  return (
    <button onClick={props.funcion} id={props.id} className={props.className}>
      <svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="50" cy="50" r="48" fill="#A2EF8A" stroke="black" stroke-width="4"/>
<path d="M50 91L50 9" stroke="black" stroke-width="10" stroke-linecap="round"/>
<path d="M91 50L8 50" stroke="black" stroke-width="10" stroke-linecap="round"/>
</svg>

    </button>
  )
}

export default BotonAgregar