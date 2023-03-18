import asyncio

import guilded_bot, discord_bot
import logging
import threading
from dotenv import load_dotenv
load_dotenv(override=True)
discord_loop = asyncio.new_event_loop()
guilded_loop = asyncio.new_event_loop()
class DiscordThread(threading.Thread):
    def run(self):
        try:
            discord_bot.start(discord_loop)
        except Exception as e:
            print(e)

class GuildedThread(threading.Thread):
    def run(self):
        guilded_bot.start(guilded_loop)

for module_name in ['discord', 'guilded']:
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'{module_name}.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

print('Starting bots...')
discord = DiscordThread()
discord.daemon = True
discord.start()
guilded = GuildedThread()
guilded.daemon = True
guilded.start()

while guilded.is_alive() and discord.is_alive():
    pass