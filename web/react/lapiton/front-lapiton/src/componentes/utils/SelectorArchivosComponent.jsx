import React from 'react'
import "../css/SelectorArchivosComponent.css"


function SelectorArchivos(props) {
  return (
    <div className='div-selector'>
      <input type="file" accept=".jpg, .jpeg, .png" id={props.id} onChange={props.funcion} className={props.className} />
      <label htmlFor="id-selector"></label>
    </div>
  )
}

export default SelectorArchivos