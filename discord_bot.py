import discord
import os
import json
import requests

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = discord.Bot(intents=intents, debug_guilds=[954366387424473088])
webhook_url = "https://media.guilded.gg/webhooks/7823bbac-b806-4b55-ac84-03bcfa3b9d47/6OzyzyfuWQ0GmwouskIuUyEG8aY8ywyGmkOmYeGCU8084oy8MGkw2qouUsSkIQAqW8mucWCkm4KwWSugEMESI4"

@bot.event
async def on_ready():
    print('Discord bot is ready...')

@bot.event
async def on_message(message: discord.Message):
    if message.channel.id != 1049833019109802035 or message.author.bot:
        return
    print(message.author, message.content)
    data = {
        "content": message.content,
        "username": message.author.display_name,
        "avatar_url": message.author.display_avatar.url
    }
    response = requests.post(webhook_url, data=json.dumps(data),
                             headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        print('Unable to send webhook')

def start(loop):
    print('Starting Discord bot')
    bot.run(os.getenv('DISCORD_TOKEN'))
    return