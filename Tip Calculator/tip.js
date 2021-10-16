function calculate(){
    let amount = document.getElementById("amount");
    let percentage = document.getElementById("percentage");

    let totalAmount = document.getElementById("totalAmount");
    let tip = document.getElementById("tip");

    totalAmount.value =parseFloat(amount.value) + parseFloat(((percentage.value/100)*amount.value));
    tip.value =(percentage.value/100)*(amount.value);
    
}