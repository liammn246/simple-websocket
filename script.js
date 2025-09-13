const chat_form = document.getElementById("chat-form");
const chat_input = document.getElementById("chat-input");
const username_input = document.getElementById("username-input");
const chat_div = document.getElementById("chat-box");
const username = document.getElementById("username-form")
let ws;

const disableChat = () => {
    chat_input.disabled = true;
    chat_div.style.backgroundColor = "lightgray";
    chat_form.style.backgroundColor = "lightgray";
}
const enableChat = () => {
    chat_input.disabled = false;
    chat_form.style.backgroundColor = "white";
    chat_div.style.backgroundColor = "white";
    username.style.display = "none";
}

disableChat()

document.getElementById("chat-form").addEventListener("submit", (e) => {
    e.preventDefault();
    ws.send(JSON.stringify({'message':chat_input.value}));
    chat_input.value = "";
    const message_box = document.getElementById("message-box");
    message_box.scrollTop = message_box.scrollHeight;
})

document.getElementById("username-form").addEventListener("submit", (e) => {
    e.preventDefault()
    enableChat()
    ws = new WebSocket(`ws://127.0.0.1:8000/ws`);
    ws.addEventListener("open", () => {
        ws.send(JSON.stringify({'username':username_input.value}));
    })
    ws.onmessage = (event) => {
        console.log("working")
        const li = document.createElement("li");
        li.classList.add("text-message")
        li.textContent = event.data;
        document.getElementById("messages-list").appendChild(li);
}
})