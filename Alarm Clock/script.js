let hour = document.getElementById("hour");
let minute = document.getElementById("minute");
let second = document.getElementById("second");
let container = document.getElementById("container");
let alarmHour = document.getElementById("alarmHour");
let alarmMinute = document.getElementById("alarmMinute");
let setHour = document.getElementById("setHour");
let setMinute = document.getElementById("setMinute");
let period = document.getElementById("time");
let period2 = document.getElementById("period");
const audio = document.getElementById("song");

//display the time
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

setInterval(time, 1000);


//show the set Alarm display
function showAlarm() {
    container.style.display = "inline-block";
}

//clear the alarms

function clearAlarms() {
    container.style.display = "none";
    setMinute.innerHTML = "00";
    setHour.innerHTML = "00";
    alarmHour.value = "";
    alarmMinute.value = "";
    audio.pause()
}

function setAlarm() {
    setHour.innerHTML = alarmHour.value;
    setMinute.innerHTML = alarmMinute.value;
    period2.innerHTML = period.value;
    if (setHour.innerHTML.length == 1) {
        setHour.innerHTML = "0" + setHour.innerHTML;
    }

    if (setMinute.innerHTML.length == 1) {
        setMinute.innerHTML = "0" + setMinute.innerHTML;
    }
}

function checkAlarm() {
    if ((hour.innerHTML == setHour.innerHTML) && (minute.innerHTML == setMinute.innerHTML)){
        console.log("Time Up");
        audio.play()
    }
}
setInterval(checkAlarm, 1000);

/* i have done it but the only problem is to allow the user to set more than one alarms
and also to place "0" infront of numbers whose length are less than 2
and also how to take into consideration the "pm" and "am" 
*/

