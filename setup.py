import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

print("Welcome to the YACB setup!")
print("Please enter your OpenAI API key below.")

while True:
    api_key = input("OpenAI API key: ")
    config['openai']['api_key'] = api_key
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("API key updated in config.ini")

    # Verify that the API key is valid by trying to create a completion with it
    try:
        import openai
        openai.api_key = api_key
        openai.Completion.create(engine="text-davinci-003", prompt="Hello", max_tokens=5)
        print("API key is valid")
        break
    except Exception as e:
        print(f"API error: {e}")
        print("API key is invalid, please try again")

# Copy chat.py to /usr/local/bin and make it executable
os.system("sudo cp yacb.py /usr/local/bin/yacb")
os.system("sudo chmod +x /usr/local/bin/yacb")
print("chatbot installed in /usr/local/bin")
