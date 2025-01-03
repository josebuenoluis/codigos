import React from "react";
import '../hojas-estilo/Boton.css'
import { exp } from "mathjs";

function Boton(props) {

    const esOperador = valor => {
        return isNaN (valor) && valor !== '.';
    }

    return (
        <button className={`boton-contenedor ${esOperador(props.children) ? 'operador' : ''}`}
        onClick={() => props.manejarClick(props.children)}>
            {props.children}
        </button>
    );
}


export default Boton;