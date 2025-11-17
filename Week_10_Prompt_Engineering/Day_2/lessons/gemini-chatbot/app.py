# Chatbot application using Google Vertex AI Gemini models
import vertexai
from vertexai.preview.language_models import ChatModel

# Replace with your project ID and region
PROJECT_ID = "my-gemini-project-478415"
REGION = "us-central1"

# Configure Vertex AI
vertexai.init(project=PROJECT_ID, location=REGION)


def generate_response(user_message, chat_history, model_choice):
    # 1) Load the Gemini modelx
    chat_model = ChatModel.from_pretrained(model_choice)

    # 2) Start a new chat session with a system prompt
    chat = chat_model.start_chat(system_message="You are a helpful assistant.")

    # 3) Replay the conversation history for context
    for user, bot in chat_history:
        chat.add_user_message(user)
        if bot:
            chat.add_response(bot)

    # 4) Add the latest user message
    chat.add_user_message(user_message)

    # 5) Send to Gemini and receive the assistant's reply
    response = chat.send()
    bot_reply = response.text.strip()

    # 6) Update the chat history and clear the input
    chat_history.append((user_message, bot_reply))
    return chat_history, ""

# Building the full Gradio UI 
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 Gemini Chatbot for Beginners")

    with gr.Row():
        # Left: Conversation window
        chatbot = gr.Chatbot(elem_id="chatbot", height=400)

        # Right: Controls column
        with gr.Column():
            txt = gr.Textbox(show_label=False, placeholder="Type your message and hit Send")
            model = gr.Dropdown(
                choices=["gemini-1.5-flash-001", "gemini-1.5-pro-001"],
                value="gemini-1.5-flash-001",
                label="Choose a model"
            )
            send = gr.Button("Send")
            clear = gr.Button("Clear Chat")

    # Wire up the buttons to your function
    send.click(fn=generate_response, inputs=[txt, chatbot, model], outputs=[chatbot, txt])
    clear.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.launch()