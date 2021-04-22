import discord
from discord.ext import commands
import os
import config
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(case_insensitive=True,intents=intents,command_prefix=config.prefix,help_command=None)
with os.scandir('.') as it:
    for entry in it:
        if entry.is_dir():
            if not (entry.name.endswith('.vs') or entry.name.endswith('__')):
                for filename in os.listdir(f'./{entry.name}'):
                    if filename.endswith('.py'):
                        bot.load_extension(f'{entry.name}.{filename[:-3]}')
                    else:
                        pass

bot.run(config.token)