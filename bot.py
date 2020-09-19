import os
import discord
import random
from dotenv import load_dotenv

load_dotenv(dotenv_path="token.env")
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
just_sent = None

@client.event
async def on_ready():
    print(f"Fax has connected to Discord!")

@client.event
async def on_message(message):
    global just_sent
    facts = [
        "Mansik is forever",
        "Tarun Pakistani",
        "Tushar sucks at Valorant",
        "Raghu is single",
        "Mansi isn't as innocent as she acts",
        "We all should've taken Arts",
        "The only thing I'm still unsure about is Sameer's relationship status",
        "We need Shayri Sangram again"
    ]

    if message.content.lower() == "spit fax":
        new_list = facts.copy()

        if just_sent is not None:
            new_list.remove(just_sent)

        random.shuffle(new_list)
        just_sent = random.choice(new_list)
        await message.channel.send(just_sent)

client.run(TOKEN)
