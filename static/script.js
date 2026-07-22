const mic = document.getElementById("mic-btn");
const input = document.getElementById("question");
const form = document.getElementById("chat-form");

mic.onclick = function () {

    input.value = "__VOICE__";

    form.submit();

};

document.addEventListener("keydown", function(event){

    if(event.key==="F1"){

        event.preventDefault();

        input.value="__VOICE__";

        form.submit();

    }

    else if(event.key==="Escape"){

        event.preventDefault();

        location.reload();

    }

});