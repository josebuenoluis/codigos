let canvas = document.getElementById("myChart");
let canvas2 = document.getElementById("myChart2");
let ctx = canvas.getContext("2d");
let ctx2 = canvas2.getContext("2d");
let myChart = new Chart(ctx,{
    type:"bar",
    data:{
        labels:["col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"],
        datasets:[{
            label:"Num datos",
            data:[10,9,15,8,7,6,5,4,3,2],
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