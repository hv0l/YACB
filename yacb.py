import configparser
import openai
import pickle
from termcolor import colored

config = configparser.ConfigParser()
config.read('config.ini')

openai.api_key = config['openai']['api_key']
models = {
    'first': config['models']['first'],
    'second': config['models']['second']
}

try:
    with open('memory.pickle', 'rb') as handle:
        memory = pickle.load(handle)
except FileNotFoundError:
    memory = {}

while True:
    message = input("You: ")
    if message == "exit":
        break

    if message in memory:
        response = memory[message]
    else:
        response = openai.Completion.create(engine=models['first'], prompt=message, max_tokens=2048, temperature=0.9).choices[0].text.strip()
        if not response or "don't understand" in response.lower() or "not sure" in response.lower():
            response = openai.Completion.create(engine=models['second'], prompt=message, max_tokens=2048, temperature=0.9).choices[0].text.strip()

        memory[message] = response

    print(colored("GPT: ", "green") + response)
    with open('memory.pickle', 'wb') as handle:
        pickle.dump(memory, handle, protocol=pickle.HIGHEST_PROTOCOL)
