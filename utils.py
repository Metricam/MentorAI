from openai import AzureOpenAI
import os
import time
# from dotenv import load_dotenv
# dotenv_path = '.env'
# load_dotenv(dotenv_path)

client = AzureOpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),  
    api_version=os.environ.get('OPENAI_API_VERSION'),
    azure_endpoint=os.environ.get("OPENAI_API_BASE")
)

def get_initial_message():
    """
    Reads the content of the 'initial_message.txt' file and returns it as a string.
    
    Returns:
        str: The content of the 'initial_message.txt' file.
    """
    with open("initial_message.txt", "r") as file:
        initial_message = file.read()
    return initial_message

def get_context():
    """
    Reads the content from the 'context.txt' file and returns it as a list with a single dictionary.
    
    Returns:
        list: A list containing a single dictionary representing a message in the conversation context.
    """
    with open("context.txt", "r") as file:
        context = file.read()
    return [{"role": "system", "content": context}]

def add_message(messages, message, role):
    """
    Adds a new message to the list of messages.

    Parameters:
    - messages (list): The list of messages.
    - message (str): The content of the message.
    - role (str): The role of the message (e.g., 'user', 'assistant').

    Returns:
    None
    """
    messages.append({"role": role, "content": message})

def get_response(messages):
    """
    Generates a response using the OpenAI GPT-3 model.

    Parameters:
    messages (list): A list of messages exchanged in the conversation.

    Returns:
    generator: The generated response (a generator).

    Raises:
    None

    """
    chat_completion = client.chat.completions.create(
        model="gpt-35-turbo-16k",
        messages=messages,
        temperature=0,
        stream=True
    )
    return chat_completion
