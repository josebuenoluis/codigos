import { useState, useEffect } from 'react'
import './App.css'

import BotonClear from './components/BotonClear.jsx';
import BotonBack from './components/BotonBack.jsx';
import Boton from './components/Boton.jsx';
import Pantalla from './components/Pantalla.jsx';

import { evaluate, prodDependencies, re } from 'mathjs';

function App() {

  const [input, setInput] = useState('0');
  const [calculos, setCalculos] = useState('');

  const [operacion,setOperacion] = useState(false);

  const agregarInput = valor => {
    if(!operacion && input.length <= 20){
      if (input === "0") {
        if ("0123456789".includes(valor)) {
          setInput("");
          setInput(valor);
        }else if("/*-+".includes(valor)){
          if (validarOperador()){
            setInput(input + valor);
          }else if(valor=="-"){
            if(validarNegativo()){
              setInput(input+valor);
            }
          }
        }
      }else{
        if("0123456789".includes(valor)){
          setInput(input + valor);
        }else if(valor === "."){
          if (validarDecimal()){
            setInput(input + valor);
          }
        }else if("/*-+".includes(valor)){
          if (validarOperador()){
            setInput(input + valor);
          }else if(valor=="-"){
            if(validarNegativo()){
              setInput(input+valor);
            }
          }
        }
      }
    }
    else if(input.length <= 20){
      console.log("En agregar input: "+input);
      setOperacion(false);
      setInput("0");
      if("0123456789".includes(valor)){
        setInput(valor);
      }else if("/*-+".includes(valor)){
       if (validarOperador()){
         setInput(input + valor);
       }
      }else if(valor === "."){
        if (validarDecimal()){
          setInput(input + valor);
        }
      }
    }
  }
  
  const validarDecimal = () => {
    let valido = false;
    let inputSplit = "";
    try{
      inputSplit = input.toString().split(/[\+\-\*\/]/);
    }catch(e){
      inputSplit = input.toString();
    }
    let ultimoNumero = inputSplit.at(-1);
    console.log("En validar decimal: "+ultimoNumero+" - "+inputSplit);
    if (!ultimoNumero.includes(".")) {
      valido = true;
    
    } else {  
      valido = false;
    }
    return valido;
  }

  const validarOperador = () => {
    let valido = false;
    let inputSplit = "";
    try{
      inputSplit = input.split(/[\+\-\*\/]/);
    }catch(e){
      inputSplit = "";
    }
    let ultimoNumero = inputSplit.at(-1);
    if (ultimoNumero === "") {
      valido = false;
    }
    else if(ultimoNumero === "-"){
      console.log("En validar operador: "+ultimoNumero);
      valido = true;
    }else{
      valido = true;
    }
    return valido;
  }

  const validarOperacion = () => {
    let valido = false;
    try{
      evaluate(input)
      valido = true;
    }
    catch(e){
      valido = false;
    }
    return valido;
  }

  const calcularResultado = () => {
    if(input){
      if (validarOperacion()){
        setCalculos("="+input);
        setInput(evaluate(input).toString());
        setOperacion(true);
      }
    }else{
      alert("Por favor ingresar valores.");
    }  
  };
    const handleTeclado = (event) => {
      if ("0123456789".includes(event.key)) {
        agregarInput(event.key);
      }else if ("+-*/.".includes(event.key)) {
        if(validarOperador()){
          if(event.key === "."){
            if(validarDecimal()){
              agregarInput(event.key);
            };
          }else{
            agregarInput(event.key);
          }
        }else if(event.key=="-"){
          if(validarNegativo()){
            agregarInput(event.key);
          }
        }
      }
      else if (event.key === "Enter") {
        calcularResultado();
      }else if(event.key === "Escape"){
        setInput("0");
      }else if(event.key === "Backspace"){
        retroceso();
      }
    };

    const validarNegativo = () => {
      let valido = false;
      let conteoNegativo = input.slice(-2,-1).split("-").length - 1;
      if(conteoNegativo == 0){
        valido = true;
      }

      return valido;
    }

    const retroceso = () => {
      setInput(input.toString().slice(0,-1))
      if(input.toString().length <= 1){
        setInput("0");
      }
    }

    useEffect(() => {
      window.addEventListener('keyup', handleTeclado);
      return () => {
        window.removeEventListener('keyup', handleTeclado);
      };
    });

  return (
    <div className="App">
      <div className="contenedor-calculadora" onKeyUp={(e) => agregarInput(e.key)}>
        <Pantalla numeros={input} calculos={calculos}/>
        <div className="fila">
          <Boton manejarClick={agregarInput} operacion={operacion}>1</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>2</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>3</Boton>
          <Boton manejarClick={agregarInput}>+</Boton>
        </div>
        <div className="fila">
          <Boton manejarClick={agregarInput} operacion={operacion}>4</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>5</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>6</Boton>
          <Boton manejarClick={agregarInput}>-</Boton>
        </div>
        <div className="fila">
          <Boton manejarClick={agregarInput} operacion={operacion}>7</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>8</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>9</Boton>
          <Boton manejarClick={agregarInput}>*</Boton>
        </div>
        <div className="fila">
          <Boton manejarClick={calcularResultado}>=</Boton>
          <Boton manejarClick={agregarInput} operacion={operacion}>0</Boton>
          <Boton manejarClick={agregarInput}>.</Boton>
          <Boton manejarClick={agregarInput}>/</Boton>
        </div>
        <div className="fila">
          <BotonClear manejarClear={() => setInput("0")}>C</BotonClear>
          <BotonBack manejarClear={retroceso}>CE</BotonBack>
        </div>
      </div>
    </div>
  )
}

export default App
