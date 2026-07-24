const mic = document.getElementById("mic-btn");
const input = document.getElementById("question");
const form = document.getElementById("chat-form");

const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;

if(!SpeechRecognition){

    alert("Speech Recognition is not supported in this browser.");

}

else{

    const recognition = new SpeechRecognition();

    recognition.lang = "en-IN";
    recognition.interimResults = false;
    recognition.continuous = false;

    mic.onclick = function(){

        mic.classList.add("listening");

        recognition.start();

    };

    recognition.onresult = function(event){

        const text = event.results[0][0].transcript;

        input.value = text;

        form.submit();

    };

    recognition.onend = function(){

        mic.classList.remove("listening");

    };

}

document.addEventListener("keydown",function(event){

    if(event.key==="F1"){

        event.preventDefault();

        mic.click();

    }

    else if(event.key==="Escape"){

        event.preventDefault();

        location.reload();

    }

});