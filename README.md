# Telegram ChatGPT Chatbot

## Prerequisites
To run the Telegram ChatGPT chatbot, ensure you have a Telegram bot and a paid OpenAI account.
openai and telebot must be installed.

### Step 1: Create a Telegram Bot
- Generate a new Telegram bot.
- Save the bot's authentication code.
- Store this code in a file named `tel_auth.txt`.

### Step 2: Set Up A Paid OpenAI Account
- Create a new OpenAI account or upgrade your current account to a paid version.
- Save your OpenAI authentication key.
- Store this key in a file named `ai_auth.txt`.

### Step 3: Copy Authentication Files
- Copy both `tel_auth.txt` and `ai_auth.txt` files.
- Paste these files in the same directory where `telegram_chatbot.py` is located.

### Step 4: Run the Chatbot
- Launch the Telegram ChatGPT chatbot by running the following command:

```shell
nohup python telegram_chatbot.py &
```
This command will ensure that the chatbot keeps running even after you log out of your terminal.