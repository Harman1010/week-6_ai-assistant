import uuid

import gradio as gr
import requests


API_URL = "http://127.0.0.1:8000"

session_id = str(uuid.uuid4())


def upload_document(file):

    if file is None:
        return "Please select a file."

    try:
        with open(file, "rb") as f:
            response = requests.post(
                f"{API_URL}/documents/upload",
                files={
                    "file": f
                },
            )

        if response.ok:
            result = response.json()

            return (
                f"{result['message']}\n"
                f"Chunks: {result.get('chunks', 0)}"
            )

        return f"Upload failed: {response.text}"

    except requests.RequestException as exc:
        return f"Could not connect to backend: {exc}"


def chat(question, history):

    if not question.strip():
        return history

    try:
        response = requests.post(
            f"{API_URL}/chat/",
            json={
                "question": question,
                "session_id": session_id,
            },
        )

        if not response.ok:
            history.append(
                {
                    "role": "user",
                    "content": question,
                }
            )
            history.append(
                {
                    "role": "assistant",
                    "content": f"Error: {response.text}",
                }
            )
            return history

        result = response.json()

        answer = result["answer"]

        sources = result.get("sources", [])

        if sources:
            answer += "\n\n**Sources:**\n"

            for source in sources:
                answer += (
                    f"- `{source['document']}`"
                )

                if source.get("page_number") is not None:
                    answer += (
                        f" — page {source['page_number']}"
                    )

                answer += "\n"

        history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        return history

    except requests.RequestException as exc:

        history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": f"Could not connect to backend: {exc}",
            }
        )

        return history


with gr.Blocks(title="AI Document Assistant") as demo:

    gr.Markdown(
        """
        # AI Document Assistant

        Upload a document and ask questions about its contents.
        """
    )

    with gr.Row():

        file_input = gr.File(
            label="Upload Document",
            file_types=[".pdf", ".txt", ".md"],
            type="filepath",
        )

        upload_button = gr.Button("Upload")

    upload_status = gr.Textbox(
        label="Upload Status",
        interactive=False,
    )

    chatbot = gr.Chatbot(
        label="Conversation",
        type="messages",
    )

    question = gr.Textbox(
        label="Question",
        placeholder="Ask a question about your documents...",
    )

    send_button = gr.Button("Send")

    upload_button.click(
        fn=upload_document,
        inputs=file_input,
        outputs=upload_status,
    )

    send_button.click(
        fn=chat,
        inputs=[question, chatbot],
        outputs=chatbot,
    )

    question.submit(
        fn=chat,
        inputs=[question, chatbot],
        outputs=chatbot,
    )


if __name__ == "__main__":
    demo.launch()