import React from 'react'
import "../css/DescripcionComponent.css"

function DescripcionComponent(props) {
  return (
    <textarea name="descripcion" className='descripcion-component'
    placeholder={props.placeholder} id={props.id}>

    </textarea>
  )
}

export default DescripcionComponent