import React from "react";
import '../hojas-estilo/BotonClear.css'

const BotonBack = (props) => (
    <div className="boton-back" onClick={props.manejarClear}>
        {props.children}
    </div>
)

export default BotonBack;