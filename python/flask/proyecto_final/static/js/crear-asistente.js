


function generarCodigoAsistente() {
    let input = document.getElementById("codigo");
    const caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let codigo = '';
    for (let i = 0; i < 6; i++) {
        const indiceAleatorio = Math.floor(Math.random() * caracteres.length);
        codigo += caracteres[indiceAleatorio];
    }
    input.value = codigo;
}

function validarTelefono(){
    let input = document.getElementById("telefono");
    let telefono = input.value;
    let valido = false;
    if(telefono.length == 9 && !isNaN(telefono)){
        valido = true;
    }else{
        valido = false;
    }
    if(valido == false){
        if(!input.classList.contains("is-invalid")){
            input.classList.add("is-invalid");
        };
    }else{
        if(input.classList.contains("is-invalid")){
            input.classList.remove("is-invalid");
        };
        if(!input.classList.contains("is-valid")){
            input.classList.add("is-valid");
        }
    }
}

function validarNif(){
    let input = document.getElementById("nif");
    let nif = input.value.toUpperCase();
    let letras = "TRWAGMYFPDXBNJZSQVHLCKE";
    let valido = false;
    let nifNumeros = nif.substring(0,8);
    if(nif.length == 9 || letras.includes(nif.at(-1))){
        valido = false;
        if(nifNumeros.at(0) == "X"){
            nifNumeros = "0" + nifNumeros.substring(1,8);
        }else if(nifNumeros.at(0) == "Y"){
            nifNumeros = "1" + nifNumeros.substring(1,8);
        }else if(nifNumeros.at(0) == "Z"){
            nifNumeros = "2" + nifNumeros.substring(1,8);
        }
        if(!isNaN(nifNumeros)){
            let letra = letras.charAt(nifNumeros % 23);
            if(letra == nif.at(-1)){
                valido = true;
            }else{
                valido = false;
            }
        }else{
            valido = false;
        }
    }
    if(valido == false){
        if(!input.classList.contains("is-invalid")){
            input.classList.add("is-invalid");
        };
    }else{
        if(input.classList.contains("is-invalid")){
            input.classList.remove("is-invalid");
        };
        if(!input.classList.contains("is-valid")){
            input.classList.add("is-valid");
        }
    }
}

function getData(e){
    e.preventDefault();
    let formulario = document.getElementById("form-crear-asistente");
    let formData = new FormData(formulario);
    let data = {
        nif: formData.get("nif"),
        nombre: formData.get("nombre"),
        telefono: formData.get("telefono"),
        codigo: formData.get("codigo"),
        planta: formData.get("planta")
    };
    console.log("Formulario data: ",data);
    postAsistente(data).then(data => {
        console.log(data);
        // if(data.success){
        //     alert("Asistente creado correctamente");
        // }else{
        //     alert("Error al crear el asistente");
        // }
    });
}

async function postAsistente(data){
    let url = "/asistentes/crear";
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if(response.ok){
            return response.json();
        }else{
            throw new Error("Error en la respuesta del servidor");
        }
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error(error);
    });

}