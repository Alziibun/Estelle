import json
import requests
import guilded
import os

client = guilded.Client()
webhook_url = "https://discord.com/api/webhooks/1086375307017191424/8l1ErcvEOwIPez60fTeLXX0ihTjZg-UZ89bW7ANbg5bivPGuXthVTirl7xm4kdf_VLcf"

@client.event
async def on_ready():
    print("guilded bot ready!")

@client.event
async def on_message(message: guilded.ChatMessage):
    if message.channel.id != "4fa824a4-e343-43fd-bd23-4989624c5611" or message.author.bot:
        return
    data = {
        "username": message.author.display_name + " (from Guilded)",
        "avatar_url": message.author.avatar.url,
        "content": message.content
    }
    requests.post(webhook_url, data=json.dumps(data),
                  headers={"Content-Type": "application/json"})


def start(loop):
    print('Starting Guilded bot...')
    client.loop = loop
    client.run(os.getenv('GUILDED_TOKEN'))