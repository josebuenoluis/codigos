import React from 'react'
import "../css/InputTextComponent.css"

function InputTextComponent(props) {
  return (
    <input type={props.type} className={props.className}
     id={props.id} placeholder={props.placeholder}/>
  )
}

export default InputTextComponent;