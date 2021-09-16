//assigning the variables
let hours = document.getElementById("hours");
let minutes = document.getElementById("minutes");
let seconds = document.getElementById("seconds");

let hourHand = document.getElementById("hourHand");
let minuteHand = document.getElementById("minuteHand");
let secondHand = document.getElementById("secondHand");


//function to input the values
function inputValues(){
    hourHand.innerHTML = hours.value;
    minuteHand.innerHTML = minutes.value;
    secondHand.innerHTML = seconds.value;
    if(hours.value == ""){
        hourHand.innerHTML = "00";
    }
    if(minutes.value == ""){
        minuteHand.innerHTML = "00";
    }
    if(seconds.value == ""){
        secondHand.innerHTML = "00";
    }
    /*
    if(hourHand.innerHTML.length <=  1){
        hourHand.innerHTML = "0" + hourHand.innerHTML;
    }
    if(secondHand.innerHTML.length <=  1){
        secondHand.innerHTML = "0" + secondHand.innerHTML;
    }
    if(minuteHand.innerHTML.length <=  1){
        minuteHand.innerHTML = "0" + minuteHand.innerHTML;
    }
    */
    
}

//function to start the countdown
function start(){
    a = setInterval(started,1000);
}

//main countdown function
function started(){
    secondHand.innerHTML--;
    if(secondHand.innerHTML == "0"){
        minuteHand.innerHTML--;
        secondHand.innerHTML = "59";
        
        

        if(minuteHand.innerHTML == "0"){
            hourHand.innerHTML--;
            minuteHand.innerHTML = "59";
            
          
            if(hourHand.HTML == "-1"){
                clearInterval(a);
        }
        }
    }
    
    
    
}
function reset(){
    
    secondHand.innerHTML = "00";
    hourHand.innerHTML = "00";
    minuteHand.innerHTML = "00";
    clearInterval(a);
}

function stop(){
    clearInterval(a);
}

