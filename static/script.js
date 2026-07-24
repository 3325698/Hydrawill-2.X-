const robot = document.querySelector(".robot");
const mic = document.getElementById("mic-btn");
const input = document.getElementById("question");
const form = document.getElementById("chat-form");

const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;

let firstLoad = true; 

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
        robot.classList.add("listening"); 
        recognition.start();

    };

    recognition.onresult = function(event){

        const text = event.results[0][0].transcript;

        input.value = text;
        
        robot.classList.remove("listening");
        robot.classList.add("thinking");

        speechSynthesis.cancel();
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

    else if(event.code==="Space"){

    event.preventDefault();

    stopSpeaking();

    }

});

// ---------- Browser Speech ----------
function stopSpeaking(){

    speechSynthesis.cancel();

    robot.classList.remove("speaking");

}

function speak(text){

    speechSynthesis.cancel();
    robot.classList.remove("thinking");
    robot.classList.add("speaking");  
    const msg = new SpeechSynthesisUtterance(text);

    msg.lang = "en-US";

    msg.rate = 1;

    msg.pitch = 1;

    const voices = speechSynthesis.getVoices();

    const female = voices.find(v =>
        v.lang.startsWith("en") &&
        v.name.toLowerCase().includes("female")
    );

    if(female){
        msg.voice = female;
    }

    speechSynthesis.speak(msg);
    msg.onend=function(){

    robot.classList.remove("speaking");

};

}

const observer = new MutationObserver(function(){

    const bots = document.querySelectorAll(".bot-text");

    if(bots.length===0) return;

    const latest = bots[bots.length-1];

    if(firstLoad){

    firstLoad = false;

    return;

    }

    speak(latest.innerText);

});

observer.observe(document.body,{
    childList:true,
    subtree:true
}); 