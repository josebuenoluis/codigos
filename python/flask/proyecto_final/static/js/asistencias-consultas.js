let canvas = document.getElementById("myChart");
let canvas2 = document.getElementById("myChart2");
let ctx = canvas.getContext("2d");
let ctx2 = canvas2.getContext("2d");
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
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});