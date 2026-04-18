const chat = document.getElementById("chat");
const input = document.getElementById("input");
const sendBtn = document.getElementById("sendBtn");

function addMessage(text, type, id=null) {
    const div = document.createElement("div");
    div.className = `msg ${type}`;
    if (id) div.id = id;

    // 🧠 IMPORTANT: render markdown properly (ChatGPT-like)
    div.innerHTML = marked.parse(text || "");

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
    return div;
}

async function send() {
    const text = input.value.trim();
    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    const id = "ai-" + Date.now();
    const el = addMessage("", "ai", id);

    const res = await fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ message: text })
    });

    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    let result = "";

    while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        result += decoder.decode(value);

        // 🧠 LIVE markdown rendering (ChatGPT feel)
        el.innerHTML = marked.parse(result);
    }
}

sendBtn.onclick = send;

input.addEventListener("keypress", (e) => {
    if (e.key === "Enter") send();
});