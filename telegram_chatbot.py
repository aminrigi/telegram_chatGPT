######################## chatGPT ##########################3
import openai 

with open('ai_auth.txt', 'r') as file:
        # Read the entire file contents into a string
    ai_auth = file.read()
    
openai.api_key = ai_auth


response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-4", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]



def gpt_response(text):
    if not text.startswith("Pp"):
        return text
    else:
        text = text[2:]
        messages =  [{'role':'assistant', 'content':text} ]
        assistant_response = get_completion_from_messages(messages, temperature=1)
        return "\n"+assistant_response
    





##################### telegram bot ####################
import telebot
import os


with open('tel_auth.txt', 'r') as file:
        # Read the entire file contents into a string
    auth = file.read()


        
bot = telebot.TeleBot(auth)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! How can I help you?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):

    bot.reply_to(message, gpt_response(message.text))

bot.infinity_polling()

