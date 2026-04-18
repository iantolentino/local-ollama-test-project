async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value;

    if (!message) return;

    addMessage("You", message, "user");

    input.value = "";

    let res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    let data = await res.json();

    addMessage("AI", data.response, "bot");
}

function addMessage(sender, text, type) {
    let box = document.getElementById("chat-box");

    let div = document.createElement("div");
    div.classList.add("message", type);
    div.innerText = sender + ": " + text;

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}