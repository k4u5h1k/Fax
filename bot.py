import os
import discord
from random import choice
from dotenv import load_dotenv

load_dotenv(dotenv_path="token.env")
token = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    facts = [
        'Mansik is forever',
        'Tarun Pakistani',
        'Tushi sucks at Valorant',
        'Cosec be dumb AF',
    ]

    if message.content.lower() == 'spit fax':
        await message.channel.send(choice(facts))

client.run(token)
