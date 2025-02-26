from markov import make_chains, make_text
from discord import Intents, Client
import os

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

@client.event
async def on_ready():
  print(f"You have successfully logged in as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  markov_chains = make_chains(message)
  markov_text = make_text(markov_chains)
  await message.channel.send(markov_text)

client.run(os.environ("DISCORD_TOKEN"))
