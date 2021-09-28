let minutes = document.getElementById("minutes");
let seconds = document.getElementById("seconds");
let milliseconds = document.getElementById("milliseconds");

function start() {
    a = setInterval(Start, 10);
}

function Start() {
    milliseconds.innerHTML++;
    if (milliseconds.innerHTML > 99) {
        seconds.innerHTML++;
        milliseconds.innerHTML = "00";

        if (seconds.innerHTML > 59) {
            minutes.innerHTML++;
            seconds.innerHTML = "00";
        }
    }

    milliseconds.innerHTML = milliseconds.innerHTML < 10 ? "0" + milliseconds.innerHTML : milliseconds.innerHTML;

    if (seconds.innerHTML.length < 2) {
        seconds.innerHTML = "0" + seconds.innerHTML;
    }

    if (minutes.innerHTML.length < 2) {
        minutes.innerHTML = "0" + minutes.innerHTML;
    }

}

function reset() {
    clearInterval(a);
    milliseconds.innerHTML = "00";
    seconds.innerHTML = "00";
    minutes.innerHTML = "00";
}