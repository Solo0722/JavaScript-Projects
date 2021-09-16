let time = document.getElementById("time");
let hour = document.getElementById("hour");
let minute = document.getElementById("minute");
let seconds = document.getElementById("seconds");

function start(){
    a = setInterval(starts,10);
    
}
function starts(){
    seconds.innerHTML++;
    if (seconds.innerHTML > 99){
        minute.innerHTML++;
        seconds.innerHTML = "00";
    }
    if (minute.innerHTML > 59){
        hour.innerHTML++;
        minute.innerHTML = "00";
        seconds.innerHTML = "00";
    }

    if(minute.innerHTML.length == 1){
        minute.innerHTML = "0"+minute.innerHTML;
    }
    if(hour.innerHTML.length == 1){
        hour.innerHTML = "0"+hour.innerHTML;
    }
   
}
function stop(){
    clearInterval(a);
}
function reset(){
    clearInterval(a);
    seconds.innerHTML = "00";
    minute.innerHTML = "00";
    hour.innerHTML = "00";

}

