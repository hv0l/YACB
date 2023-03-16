#!/usr/bin/env python3

import configparser
import openai
import pickle
import sys
from termcolor import colored


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


def main():
    models = load_configuration()
    memory = load_memory()
    conversation_history = []

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break

        response = get_response(message, models, memory, conversation_history)
        print(colored("GPT: ", "green") + response)

        save_memory(memory)


if __name__ == '__main__':
    main()
