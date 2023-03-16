#!/usr/bin/env python3

import configparser
import openai
import pickle
import sys
from tkinter import *
from tkinter.scrolledtext import ScrolledText


def load_configuration():
    config = configparser.ConfigParser()
    config.read('config.ini')

    openai.api_key = config['openai']['api_key']
    models = {
        'first': config['models']['first'],
        'second': config['models']['second']
    }

    return models


def load_memory():
    try:
        with open('memory.pickle', 'rb') as handle:
            memory = pickle.load(handle)
    except FileNotFoundError:
        memory = {}

    return memory


def save_memory(memory):
    with open('memory.pickle', 'wb') as handle:
        pickle.dump(memory, handle, protocol=pickle.HIGHEST_PROTOCOL)


def get_response(message, models, memory, conversation_history):
    conversation_history.append(message)
    conversation_prompt = "\n".join(conversation_history)

    if conversation_prompt in memory:
        response = memory[conversation_prompt]
    else:
        response = openai.Completion.create(engine=models['first'], prompt=conversation_prompt, max_tokens=2048, temperature=0.9).choices[0].text.strip()
        if not response or "don't understand" in response.lower() or "not sure" in response.lower():
            response = openai.Completion.create(engine=models['second'], prompt=conversation_prompt, max_tokens=2048, temperature=0.9).choices[0].text.strip()

        memory[conversation_prompt] = response

    conversation_history.append(response)

    return response


def send_message():
    message = input_field.get()
    if not message:
        return

    input_field.delete(0, END)
    chat_log.config(state=NORMAL)
    chat_log.insert(END, f"You: {message}\n")
    chat_log.config(state=DISABLED)

    response = get_response(message, models, memory, conversation_history)
    chat_log.config(state=NORMAL)
    chat_log.insert(END, f"GPT: {response}\n", "gpt")
    chat_log.config(state=DISABLED)

    save_memory(memory)


models = load_configuration()
memory = load_memory()
conversation_history = []

root = Tk()
root.title("Chatbot")

frame = Frame(root)
scrollbar = Scrollbar(frame)
chat_log = ScrolledText(frame, wrap=WORD, state=DISABLED, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
chat_log.pack(side=LEFT, fill=BOTH, expand=True)
frame.pack(fill=BOTH, expand=True)

chat_log.tag_configure("gpt", foreground="green")

input_field = Entry(root)
input_field.pack(fill=X, padx=5, pady=5)
input_field.bind('<Return>', lambda event: send_message())

send_button = Button(root, text="Send", command=send_message)
send_button.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
