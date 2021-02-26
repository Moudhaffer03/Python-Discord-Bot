import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "pissed", "pissed off", "feeling down", "feeling blue", "crying", "miserable"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  
  return quote

@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
    msg = message.content
    if msg.startswith('!inspire') or any(word in msg for word in sad_words):
      quote = get_quote()
      await message.channel.send(quote)

client.run(os.getenv('TOKEN'))