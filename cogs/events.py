from discord.colour import Color
from discord.ext import commands
import discord
from discord import user
from discord import member
import json
import datetime
from discord.ext.commands.errors import CheckFailure, CommandNotFound, CommandOnCooldown, MissingPermissions, MissingRequiredArgument, NotOwner
import asyncio

class Events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in")
        with open('cogs/cooldown.json', 'r') as f:
            cds = json.load(f)
        for key,value in list(cds.items()):
            cds[str(key)] = False
        with open('cogs/cooldown.json', 'w') as file:
            json.dump(cds,file,indent=4)
    
    @commands.Cog.listener()
    async def on_message(self,message):
        me = await self.bot.fetch_user('449555448010375201')
        msg = message.content
        if isinstance(message.channel, discord.channel.DMChannel):
            if message.author == self.bot.user:
                return
            if message.author.id == me.id:
                pass
            else:
                embedvar = discord.Embed(title="Message from " + str(message.author), 
                timestamp=datetime.datetime.utcnow(), 
                colour=discord.Colour(0xe74c3c))
                embedvar.add_field(name="Message Content: ", value = msg)
                embedvar.set_thumbnail(url=message.author.avatar_url)
                embedvar.set_footer(text="Sender's ID: " + str(message.author.id))
                await me.send(embed=embedvar)
                print(me)
        if not message.author.bot:
            ok = False
            with open('cogs/reps.json', 'r') as f:
                rep = json.load(f)
            for key,value in list(rep.items()):
                if str(message.author.id) == key:
                    ok=True
            if ok == False:        
                rep[str(message.author.id)] = 0
                print(1)
                with open('cogs/reps.json', 'w') as file:
                    json.dump(rep,file,indent=4)
                   
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error,CommandNotFound):
            embed = discord.Embed(title=f"```❌'{ctx.message.content}' is an invalid command!```",color = discord.Colour.red(),timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="Use ..help to see avaiable commands", icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, MissingPermissions):
            await ctx.send(f"{ctx.message.author.mention}, you don't meet the requirements")
        else:
            raise error
    

def setup(bot):
    bot.add_cog(Events(bot))