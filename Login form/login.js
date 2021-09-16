function openNav(){
    let login = document.getElementById("login");
    let header = document.getElementById("header");
    let mainbtn = document.getElementById("main");
    login.style.width = "300px";
    mainbtn.style.width = "0%";
    
}

function closeNav(){
    let login = document.getElementById("login");
    login.style.width = "0px";
    let mainbtn = document.getElementById("main");
    mainbtn.style.width = "70px";
    let header = document.getElementById("header");
}