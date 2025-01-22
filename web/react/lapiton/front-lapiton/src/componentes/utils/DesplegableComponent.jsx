import React from 'react'
import "../css/DesplegableComponent.css"
function DesplegableComponent() {
  return (
    <div className='input-desplegable'>
      <select name="categoria-filtro" id="categoria-seleccionada">
        <option value="">Por favor selecciona una categoria</option>
      </select>
    </div>
  )
}

export default DesplegableComponent
