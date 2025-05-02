let canvas = document.getElementById("myChart");
let canvas2 = document.getElementById("myChart2");
let canvas3 = document.getElementById("myChart3");
let ctx = canvas.getContext("2d");
let ctx2 = canvas2.getContext("2d");
let ctx3 = canvas3.getContext("2d");
let myChart = new Chart(ctx,{
    type:"bar",
    data:{
        labels:['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
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
        labels:['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First Dataset',
            data: [65, 59, 80, 81, 56, 55, 40],
            fill: false,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
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
        labels:["col1","col2"],
        datasets:[{
            label:"Num datos",
            data:[10,4],
            backgroundColor:[
                "rgba(255, 99, 132, 0.5)",
                "rgba(54, 162, 235, 0.5)",
            ],
        }]
    },
});

