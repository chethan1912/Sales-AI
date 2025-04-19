async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    appendMessage("You", message);

    const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: message })
    });

    const data = await res.json();
    appendMessage("Bot", data.response);
    input.value = "";
}

function appendMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const msgDiv = document.createElement("div");
    msgDiv.textContent = `${sender}: ${text}`;
    chatBox.appendChild(msgDiv);
}
