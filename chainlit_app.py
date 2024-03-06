import chainlit as cl
import time
from utils import get_initial_message, get_context, add_message, get_response

messages = get_context()

# chainlit run chainlit_app.py -w

@cl.on_chat_start
async def start():
    
    initial_message = get_initial_message()

    # Add ChatGPT's response to the messages list
    add_message(messages, initial_message, "assistant")

    await cl.Message(
        content=initial_message,
    ).send()


@cl.on_message
async def main(message: cl.Message):
    # Initialize the ChainLit message (for streaming purposes)
    msg = cl.Message(content="")

    # Add users message to the messages list
    add_message(messages, message.content, "user")

    # Get a response from ChatGPT
    chat_response = get_response(messages)
    chat_message = ""

    # Stream the response from ChatGPT
    for chunk in chat_response:
        if len(chunk.choices) == 0:
            continue

        delta = chunk.choices[0].delta

        if delta.content:
            chat_message += delta.content
            await msg.stream_token(delta.content)

    # Add ChatGPT's response to the messages list
    add_message(messages, chat_message, "assistant")

    # Send a response back to the user
    await msg.send()

@cl.on_chat_end
def on_chat_end():
    pass