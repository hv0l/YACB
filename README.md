YACB - Yet Another Chatbot
==========================
```

      _____                    _____                    _____                    _____          
     |\    \                  /\    \                  /\    \                  /\    \         
     |:\____\                /::\    \                /::\    \                /::\    \        
     |::|   |               /::::\    \              /::::\    \              /::::\    \       
     |::|   |              /::::::\    \            /::::::\    \            /::::::\    \      
     |::|   |             /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
     |::|   |            /:::/__\:::\    \        /:::/  \:::\    \        /:::/__\:::\    \    
     |::|   |           /::::\   \:::\    \      /:::/    \:::\    \      /::::\   \:::\    \   
     |::|___|______    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\   \:::\    \  
     /::::::::\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::\   \:::\ ___\ 
    /::::::::::\____\/:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/__\:::\   \:::|    |
   /:::/~~~~/~~      \::/    \:::\  /:::/    /\:::\    \      \::/    /\:::\   \:::\  /:::|____|
  /:::/    /          \/____/ \:::\/:::/    /  \:::\    \      \/____/  \:::\   \:::\/:::/    / 
 /:::/    /                    \::::::/    /    \:::\    \               \:::\   \::::::/    /  
/:::/    /                      \::::/    /      \:::\    \               \:::\   \::::/    /   
\::/    /                       /:::/    /        \:::\    \               \:::\  /:::/    /    
 \/____/                       /:::/    /          \:::\    \               \:::\/:::/    /     
                              /:::/    /            \:::\    \               \::::::/    /      
                             /:::/    /              \:::\____\               \::::/    /       
                             \::/    /                \::/    /                \::/____/        
                              \/____/                  \/____/                  ~~              
                                                                                                


                   
```
YACB is a GPT-based chatbot that uses the OpenAI API to generate responses. It is designed to be easy to use and extendable. One of its key features is the ability to maintain context during a conversation by utilizing a memory system. This allows the chatbot to provide more accurate and relevant responses based on the conversation history.

Prerequisites
-------------

1. Python 3.6 or newer
2. An OpenAI API key

Installation
------------

1. Clone the repository or download and extract the ZIP file. `https://github.com/hv0l/YACB`
2. Install the required Python libraries by running `pip install -r requirements.txt`.
3. Run the `setup.py` script to set up the chatbot: `python3 setup.py`. Follow the prompts to enter your OpenAI API key.
4. The script will save the API key in `config.ini` and will install the chatbot as an executable in `/usr/local/bin`.

Usage
-----

1. Start the chatbot by running `python3 yacb.py` or simply `yacb` if you've installed it as an executable.
2. Interact with the chatbot by typing messages and pressing Enter to send them. The chatbot will respond with a generated message.
3. To exit the chatbot, type "exit" and press Enter.

Configuration
-------------

You can configure the chatbot by editing the `config.ini` file. It contains the following sections:

1. `openai`: This section contains the OpenAI API key.
2. `models`: This section contains the names of the primary and secondary models used for generating responses.

Customization
-------------

You can further customize and extend the chatbot by modifying the `yacb.py` script. For example, you can add new features or change the chatbot's behavior.

Troubleshooting
---------------

If you encounter any issues while running the chatbot, please check the following:

1. Make sure your OpenAI API key is valid and correctly set in the `config.ini` file.
2. Ensure you have installed all the required Python libraries.

![Schermata del 2023-03-16 17-33-34](https://user-images.githubusercontent.com/61795418/225689113-3c86352d-96c3-4afd-b15d-58aeb8bdcd2c.png)

