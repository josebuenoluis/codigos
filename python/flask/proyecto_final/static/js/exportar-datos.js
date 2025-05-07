let tabla = document.getElementById("tabla-asistencias");

function obtenerAsistencias(){
    let data = [];
    let headers = [];
    let tbody = tabla.querySelector("tbody");
    let theaders = tabla.querySelector("thead");
    
    for(let header = 0; header < theaders.rows.length;header++){

    }

    for(let row = 0; row < tbody.rows.length;row++){
        let childRow = tbody.rows[row];
        let object = {};
        for(let cell = 0; cell < childRow.cells.length;cell++){
            let header = theaders.rows[0].cells[cell].textContent;
            object[header] = childRow.cells[cell].textContent;
            data.push(object)
        }
    }
    if(data.length > 0){
        postData(data).then(response =>{
            if(response.success == true){
                console.log(response);
            }else{
                console.log("Error: ",response);
            }
        });
    }
}

async function postData(data){
    let endpoint = "/asistencias/exportar"; 
    return await fetch(endpoint,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(data)
    }).then(response =>{
        return response.json();
    }).catch(error =>{
        console.log("Error: ",error);
    });
}