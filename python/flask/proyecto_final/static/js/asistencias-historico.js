let canvas = document.getElementById("myChart");
let ctx = canvas.getContext("2d");
let myChart = new Chart(ctx,{
    type:"line",
    data:{
        labels:['Enero', 'Febrero', 'Marzo', 'Abril', 'May', 'Junio', 'Julio', 
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets: [{
            label: 'Historico de asistencias',
            data: [0,0,0,0,0,0,0,0,0,0,0,0],
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
function mostrarHistorico(){
    // Cada objeto JSON es un mes de asistencias
    // [
    //     {
    //       "anio": 2025,
    //       "mes": 4,
    //       "total_asistencias": 1
    //     },
    //     {
    //       "anio": 2025,
    //       "mes": 5,
    //       "total_asistencias": 99
    //     }
    // ]
    obtenerHistorico().then(data => {
        data.forEach(element => {
            myChart.data.datasets[0].data.push(element.total_asistencias);
            myChart.update();
        });
    });
}

async function obtenerHistorico(){
    return await fetch("/api/asistencias/historico",{
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