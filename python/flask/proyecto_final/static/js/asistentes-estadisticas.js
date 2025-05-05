let canvas = document.getElementById("myChart");
let canvas2 = document.getElementById("myChart2");
let ctx = canvas.getContext("2d");
let ctx2 = canvas2.getContext("2d");
let n_atendidas = 0;
let n_no_atendidas = 0;
let asistencias_asistenes = [];

let myChart = new Chart(ctx,{
    type:"bar",
    data:{
        labels:[],
        datasets:[{
            label:"Por asistente",
            data:[],
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
            ],
            backgroundColor:[
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
                "rgba(255, 206, 86, 0.5)"
            ],
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
    type:"pie",
    data:{
        labels:["Atendidas","Pendientes"],
        datasets:[{
            label:"Asistencias totales",
            data:[],
            backgroundColor:[
              "rgba(54, 162, 235, 0.5)",
              "rgba(255, 99, 132, 0.5)",
            ],
        }]
    },
});



obtenerConteoAsistencias().then(data => {
    n_atendidas = data.asistencias_atendidas;
    n_no_atendidas = data.asistencias_pendientes;
    myChart2.data.datasets[0].data[0] = n_atendidas;
    myChart2.data.datasets[0].data[1] = n_no_atendidas;
  });

obtenerAsistenciasAsistentes().then(data => {
  let lista_asistencias = [];
  let lista_nombres = [];
  // Guardamos en la lista el numero de asistencias atendidas y 
  // nombre de asistentes
  data.forEach(element => {
    lista_nombres.push(element.nombre);
    lista_asistencias.push(element.asistencias_atendidas);
  });
  myChart.data.labels = lista_nombres;
  myChart.data.datasets[0].data = lista_asistencias;
  myChart.update();
});

function mostrarAsistenciasAsistentes(n_planta=0){
  // Para la grafica de Barras
  obtenerAsistenciasAsistentes(n_planta).then(data => {
    let lista_asistencias = [];
    let lista_nombres = [];
    // Guardamos en la lista el numero de asistencias atendidas y 
    // nombre de asistentes
    data.forEach(element => {
      lista_nombres.push(element.nombre);
      lista_asistencias.push(element.asistencias_atendidas);
    });
    myChart.data.labels = lista_nombres;
    myChart.data.datasets[0].data = lista_asistencias;
    myChart.update();
  });
  // Para la grafica de tipo Pie
  obtenerConteoAsistencias(n_planta).then(data => {
    console.log("Data: ",data);
    n_atendidas = data.asistencias_atendidas;
    n_no_atendidas = data.asistencias_pendientes;
    myChart2.data.datasets[0].data[0] = n_atendidas;
    myChart2.data.datasets[0].data[1] = n_no_atendidas;
    myChart2.update();
  });
}

function buscarAsistentes(){
    let table = document.querySelector("table");
    let tbody = table.querySelector('tbody');
    let input = document.getElementById("buscar-asistentes");
    if(tbody){
      let rows = tbody.rows;
      for (let row = 0; row < rows.length; row++) {
        let rowTable = rows[row];
        let refRowTable = rowTable.cells[1].textContent?.toLowerCase() || '';
        if (!refRowTable.includes(input.value.toLowerCase())) {
          rowTable.style.display = 'none';
        } else {
          rowTable.style.display = '';
        }
      }
    }
}

function filtrarPlanta(){
    let table = document.querySelector("table");
    let tbody = table.querySelector('tbody');
    let input = document.getElementById("planta");
    if(tbody){
      let rows = tbody.rows;
      for (let row = 0; row < rows.length; row++) {
        let rowTable = rows[row];
        let refRowTable = rowTable.cells[2].textContent?.toLowerCase() || '';
        if (!refRowTable.includes(input.value.toLowerCase())) {
          rowTable.style.display = 'none';
        } else {
          rowTable.style.display = '';
        }
      }
    }
    let n_planta = input.value == "" ? 0 : parseInt(input.value);
    mostrarAsistenciasAsistentes(n_planta);
}

async function obtenerConteoAsistencias(n_planta=0){
  let endpoint = "/api/asistencias/conteo";
  if(n_planta != 0){
    endpoint = endpoint+"/"+n_planta.toString();
  }
  return await fetch(endpoint,{
    method:"GET",
    headers:{
      "Content-Type":"application/json"
    }
  }).then(data => {
    return data.json();
  }).catch(error => {
    console.log("Error: ",error);
  })
}

async function obtenerAsistenciasAsistentes(n_planta = 0){
  let endpoint = "/api/asistentes/estadisticas";
  if(n_planta != 0){
    endpoint = endpoint+"/"+n_planta.toString();
  }
  return await fetch(endpoint,{
    method:"GET",
    headers:{
      "Content-Type":"application/json"
    }
  }).then(data => {
    return data.json();
  }).catch(error => {
    console.log("Error: ",error);
  });
}
