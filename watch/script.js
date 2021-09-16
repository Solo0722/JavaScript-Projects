let hour = document.getElementById("hour");
let minute = document.getElementById("minute");
let second = document.getElementById("second");

function time(){
    var date = new Date();
    hour.innerHTML = date.getHours();
    minute.innerHTML = date.getMinutes();
    second.innerHTML = date.getSeconds();

    if(hour.innerHTML.length <=  1){
        hour.innerHTML = "0" + date.getHours()
    }
    if(minute.innerHTML.length <=  1){
        minute.innerHTML = "0" + date.getMinutes()
    }
    if(second.innerHTML.length <=  1){
        second.innerHTML = "0" + date.getSeconds()
    }

    if(hour.innerHTML < 12){
        second.innerHTML = second.innerHTML + " AM";
        
    }
    
    else{
        second.innerHTML = second.innerHTML + " PM";
        hour.innerHTML = "0"+ (hour.innerHTML - 12);
    }
    if(hour.innerHTML == 00){
        hour.innerHTML = 12;
    }
}

setInterval(time,1000);