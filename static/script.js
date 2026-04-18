document.addEventListener("DOMContentLoaded", () => {

    const chat = document.getElementById("chat");
    const input = document.getElementById("input");
    const sendBtn = document.getElementById("sendBtn");

    function addMessage(text, type, id = null) {
        const div = document.createElement("div");
        div.className = `msg ${type}`;
        if (id) div.id = id;

        // SAFE CHECK (prevents crash)
        if (typeof marked !== "undefined") {
            div.innerHTML = marked.parse(text);
        } else {
            div.innerText = text;
        }

        chat.appendChild(div);
        chat.scrollTop = chat.scrollHeight;
    }

    function updateMessage(id, text) {
        const el = document.getElementById(id);
        if (!el) return;

        if (typeof marked !== "undefined") {
            el.innerHTML = marked.parse(text);
        } else {
            el.innerText = text;
        }
    }

    function showThinking() {
        const id = "thinking-" + Date.now();

        const div = document.createElement("div");
        div.className = "msg ai thinking";
        div.id = id;
        div.innerText = "AI is thinking...";

        chat.appendChild(div);
        chat.scrollTop = chat.scrollHeight;

        return id;
    }

    async function sendMessage() {
        const text = input.value.trim();
        if (!text) return;

        addMessage(text, "user");
        input.value = "";

        const thinkingId = showThinking();

        try {
            const res = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: text })
            });

            const data = await res.json();
            updateMessage(thinkingId, data.response);

        } catch (err) {
            updateMessage(thinkingId, "Error: " + err.message);
        }
    }

    // button event (SAFE)
    sendBtn.addEventListener("click", sendMessage);

    // ENTER key support (important UX upgrade)
    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") sendMessage();
    });

});