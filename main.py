import discord
from discord.ext import commands
import os
import config
#from dpymenus import *

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

'''
@bot.command()
async def pageembed(ctx):
    page1 = Page(title='test tile ', description="test")
    page1.add_field(name='test', value='test1')
    page2 = Page(title='test tile 2', description="test")
    page2.add_field(name='test', value='test2')
    page3 = Page(title='test tile 3', description="test")
    page3.add_field(name='test', value='test3')
    menu = PaginatedMenu(ctx)
    menu.persist_on_close()
    menu.add_pages([page1, page2, page3])
    await menu.open()
'''
bot.run(config.token)