import React from "react";
import '../hojas-estilo/Pantalla.css'

const Pantalla = ({numeros,calculos}) => (
    <div className="input">
        <div className="operacion">
            {calculos}
        </div>
        <div className="numeros">
            {numeros}
        </div>
    </div>
);

export default Pantalla;