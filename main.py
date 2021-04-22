import discord
from discord.ext import commands
import os
import config

intents = discord.Intents.all()
bot = commands.Bot(case_insensitive=True,intents=intents,command_prefix=config.prefix,help_command=None)
for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config.token)