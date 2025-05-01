const sidebar = document.querySelector(".sidebar");
const sidebarToggler = document.querySelector(".sidebar-toggler");
const sidebarTogler2 = document.querySelector(".sidebar-toggler-header");
let desplegado = false;
sidebarTogler2.addEventListener("click",() => {
    sidebar.classList.toggle("collapsed");
    if(desplegado == false){
        desplegado = true;
    }else{
        desplegado = false;
    }
    evaluarHeader();
});


function evaluarHeader(){
    const header = document.querySelector("body > header");
    const userIcon = header.querySelector(".icon-user");
    const sidebars = document.querySelector(".sidebar");
    if(window.innerWidth <= 326 && desplegado == true){
        userIcon.style.display = "none";
    }else{
        setTimeout(() => {
            userIcon.style.display = "inline";
        }, 200);
    }
    console.log(header);
    console.log(header.style.width);
}