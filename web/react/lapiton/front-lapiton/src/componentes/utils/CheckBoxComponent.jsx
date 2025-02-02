import React from 'react'
import "../css/CheckBoxComponent.css"
function CheckBoxComponent(props) {
  return (
    <div className="checkbox-container">
        <input type="checkbox" className='check-component' name={props.name} id={props.id} />
        <label htmlFor={props.id}>{props.label}</label>
    </div>
  )
}

export default CheckBoxComponent