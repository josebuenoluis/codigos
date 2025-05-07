let canvas = document.getElementById("myChart");
let canvas2 = document.getElementById("myChart2");
let canvas3 = document.getElementById("myChart3");
let ctx = canvas.getContext("2d");
let ctx2 = canvas2.getContext("2d");
let ctx3 = canvas3.getContext("2d");


mostrarEstadisticasPlantas();
mostrarAsistenciasHabitaciones();
mostrarPorcentajeAsistenciaas();
// Llamadas por planta
let myChart = new Chart(ctx,{
    type:"bar",
    data:{
        labels:[],
        datasets: [{
            label: 'Llamados por planta',
            data: [],
            fill: false,
            backgroundColor:[
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
                "rgba(255, 206, 86, 0.5)",
                "rgba(75, 192, 192, 0.5)",
                "rgba(153, 102, 255, 0.5)",
            ],
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }]
    },
    options:{
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
let myChart2 = new Chart(ctx2,{
    type:"bar",
    data:{
        labels:[],
        datasets: [{
            label: 'Habitaciones con mas llamados',
            data: [],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1,
            backgroundColor:[
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
                "rgba(255, 206, 86, 0.5)",
                "rgba(75, 192, 192, 0.5)",
                "rgba(153, 102, 255, 0.5)",
                "rgba(255, 159, 64, 0.5)",
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
                "rgba(255, 206, 86, 0.5)",
                "rgba(75, 192, 192, 0.5)"
            ]
          }]
    },
    options:{
        indexAxis:"y",
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

let myChart3 = new Chart(ctx3,{
    type:"pie",
    data:{
        labels:["No atendidas","Atendidas"],
        datasets:[{
            label:"Asistencias sobre el total",
            data:[],
            backgroundColor:[
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
            ],
        }]
    },
});

async function obtenerPlantas(){
    return await fetch("/api/plantas",{
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        },
    }).then(response => {
        if(response.ok){
            return response.json();
        }else{
            console.error("Error al obtener las plantas: ",response.statusText);
        }
    }).catch(error => {
        console.log("Error: ",error);
    })
}

async function obtenerConteoPlantas(){
    let endpoint = "/api/asistencias/plantas";
    return await fetch("/api/asistencias/plantas",{
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        }
    }).then(data =>{
        return data.json();
    }).catch(error =>{
        console.log("Error: ",error);
    });
}

function mostrarEstadisticasPlantas(){
    obtenerPlantas().then(data =>{
        console.log(data);
        myChart.data.labels = [];
        data.forEach(element => {
            myChart.data.labels.push(`Planta ${element.numero}`);
        });
        myChart.update();
    });

    // Obtenemos las estadisticas por cada planta
    obtenerConteoPlantas().then(data =>{
        data.asistencias_atendidas.forEach(element => {
            console.log(element.total_asistencias);
            myChart.data.datasets[0].data.push(element.total_asistencias);
        });
        console.log(data);
        myChart.update();
    });
}

function mostrarAsistenciasHabitaciones(){
    obtenerLlamadosHabitaciones().then(data => {
        let lista_asistencias = [];
        let lista_habitaciones = [];
        // Guardamos en la lista el numero de asistencias atendidas y 
        // nombre de asistentes
        data.forEach(element => {
          lista_habitaciones.push(element.habitacion);
          lista_asistencias.push(element.conteo_llamadas);
        });
        myChart2.data.labels = lista_habitaciones;
        myChart2.data.datasets[0].data = lista_asistencias;
        myChart2.update();
    });2
}

async function obtenerLlamadosHabitaciones(){
    let endpoint = "/api/habitaciones/asistencias/conteo";
    return await fetch(endpoint,{
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        }
    }).then(data =>{
        return data.json();
    }).catch(error =>{
        console.log("Error: ",error);
    });
}

function mostrarPorcentajeAsistenciaas(){
    obtenerPorcentajeAsistencias().then(data =>{
        console.log("Porcentajes: ",data);
        myChart3.data.datasets[0].data.push(data.porcentaje_atendidas);
        myChart3.data.datasets[0].data.push(data.porcentaje_no_atendidas);
        myChart3.update();
    });
}

async function obtenerPorcentajeAsistencias(){
    let endpoint = "/api/asistencias/porcentaje";
    return await fetch("/api/asistencias/porcentaje",{
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        }
    }).then(data => {
        return data.json();
    }).catch(error =>{
        console.log("Error: ",error);
    });
}