let canvas = document.getElementById("myChart");
let ctx = canvas.getContext("2d");
let myChart = new Chart(ctx,{
    type:"line",
    data:{
        labels:['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [{
            label: 'Historico de asistencias',
            data: [65, 59, 80, 81, 56, 55, 40, 55, 40, 65, 59, 80],
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