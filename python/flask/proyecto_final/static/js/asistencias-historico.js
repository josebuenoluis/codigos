let canvas = document.getElementById("myChart");
let ctx = canvas.getContext("2d");
let meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'May', 'Junio', 'Julio', 
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
let myChart = new Chart(ctx,{
    type:"line",
    data:{
        labels:meses,
        datasets: [{
            label: 'Historico de asistencias',
            data: [],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
          }]
    },
    options:{
        responsive:true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

mostrarHistorico();
function mostrarHistorico(desde="",hasta=""){
    
    // Cada objeto JSON es un mes de asistencias
    obtenerHistorico(desde,hasta).then(data => {
        myChart.data.labels = [];
        myChart.data.datasets[0].data = [];
        data.forEach(element => {
            myChart.data.labels.push(meses[element.mes-1]);
            myChart.data.datasets[0].data.push(element.total_asistencias);
        });
        console.log(data);
        myChart.update();
    });
}

async function obtenerHistorico(desde="",hasta=""){
    let endopoint = "/api/asistencias/historico";
    if(desde != "" && hasta != ""){
        endopoint = endopoint+`?desde=${desde}&hasta=${hasta}`;
    }
    return await fetch(endopoint,{
        method:"GET",
        headers:{
            "Content-Type":"application/json"
        },
    }).then(data => {
        return data.json();
    }).catch(error => {
        console.log("Error: ",error);
    });
}

function filtroMes(){
    let inputDesde = document.getElementById("desde");
    let inputHasta = document.getElementById("hasta");
    if(inputDesde.value != "" && inputHasta.value != ""){
        mostrarHistorico(inputDesde.value,inputHasta.value);
    }
}
