import os

import requests
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:1b")

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Security Lab Chatbot</title>
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; font-family: Arial, sans-serif; background: #f5f7fb; color: #202938; }
    .app { width: min(900px, 94%); height: 92vh; margin: 4vh auto; display: flex; flex-direction: column; background: #fff; border: 1px solid #e5e9f0; border-radius: 16px; box-shadow: 0 8px 28px rgba(20,35,60,.08); overflow: hidden; }
    header { padding: 18px 22px; border-bottom: 1px solid #e8edf3; }
    header h1 { margin: 0; font-size: 19px; }
    header p { margin: 6px 0 0; color: #778195; font-size: 12px; }
    #chat { flex: 1; overflow-y: auto; padding: 22px; }
    .message { margin: 0 0 18px; }
    .label { margin: 0 0 7px; color: #7b8494; font-size: 11px; font-weight: bold; letter-spacing: .06em; }
    .bubble { width: fit-content; max-width: min(78%, 680px); padding: 12px 15px; border-radius: 13px; line-height: 1.5; white-space: pre-wrap; overflow-wrap: anywhere; font-size: 14px; }
    .user { margin-left: auto; }
    .user .label { text-align: right; }
    .user .bubble { margin-left: auto; color: white; background: #1685e8; border-bottom-right-radius: 4px; }
    .assistant .bubble { color: #263244; background: #f0f2f5; border-bottom-left-radius: 4px; }
    .error .bubble { color: #9b2424; background: #fff0f0; }
    form { display: flex; gap: 10px; padding: 16px; border-top: 1px solid #e8edf3; }
    input { flex: 1; min-width: 0; padding: 14px 16px; border: 1px solid #d7deea; border-radius: 12px; outline: none; font-size: 14px; }
    input:focus { border-color: #1685e8; }
    button { width: 48px; border: 0; border-radius: 12px; color: white; background: #1685e8; font-size: 20px; cursor: pointer; }
    button:disabled { opacity: .55; cursor: wait; }
    .note { padding: 0 16px 12px; color: #8b94a3; text-align: center; font-size: 11px; }
    @media (max-width: 600px) { .app { height: 96vh; margin: 2vh auto; } #chat { padding: 15px; } .bubble { max-width: 90%; } }
  </style>
</head>
<body>
  <main class="app">
    <header>
      <h1>AI Assistant</h1>
      <p>Local Ollama-powered chatbot · AI Security Lab</p>
    </header>
    <section id="chat" aria-live="polite">
      <div class="message assistant">
        <div class="label">AI ASSISTANT</div>
        <div class="bubble">Hello! Ask me a question to get started.</div>
      </div>
    </section>
    <form id="chat-form">
      <input id="message" type="text" placeholder="Ask anything about cybersecurity..." autocomplete="off" required>
      <button id="send" type="submit" aria-label="Send">↑</button>
    </form>
    <div class="note">AI can make mistakes. Verify important information.</div>
  </main>
  <script>
    const form = document.getElementById("chat-form");
    const input = document.getElementById("message");
    const chat = document.getElementById("chat");
    const sendButton = document.getElementById("send");

    function addMessage(text, role) {
      const wrapper = document.createElement("div");
      wrapper.className = "message " + role;
      const label = document.createElement("div");
      label.className = "label";
      label.textContent = role === "user" ? "YOU" : "AI ASSISTANT";
      const bubble = document.createElement("div");
      bubble.className = "bubble";
      // Render model output as text, not HTML.
      bubble.textContent = text;
      wrapper.appendChild(label);
      wrapper.appendChild(bubble);
      chat.appendChild(wrapper);
      chat.scrollTop = chat.scrollHeight;
      return bubble;
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const message = input.value.trim();
      if (!message) return;
      addMessage(message, "user");
      input.value = "";
      sendButton.disabled = true;
      const reply = addMessage("Thinking...", "assistant");

      try {
        const response = await fetch("/ask", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message })
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "The request failed.");
        reply.textContent = data.response || "(The model returned an empty response.)";
      } catch (error) {
        reply.textContent = error.message || "Unable to contact the AI service.";
        reply.parentElement.classList.add("error");
      } finally {
        sendButton.disabled = false;
        input.focus();
        chat.scrollTop = chat.scrollHeight;
      }
    });
  </script>
</body>
</html>
"""


@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML)


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"error": "Message cannot be empty"}), 400

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": message,
                "stream": False
            },
            timeout=600
        )
        response.raise_for_status()
        result = response.json()

        return jsonify({"response": result.get("response", "")})

    except requests.exceptions.RequestException as error:
        return jsonify({"error": "Ollama connection failed: " + str(error)}), 502


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
