from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, CommandOnCooldown, MissingPermissions, MissingRequiredArgument, NotOwner
import datetime
import discord
import json
from asyncio.tasks import sleep
import asyncio
from discord.ext.commands import bot
reps = 0


async def timeouttask(ctx):
    await asyncio.sleep(86400)
    with open('./cooldown.json', 'r') as f:
        cds = json.load(f)
    cds[str(ctx.message.author.id)] = False
    with open('./cooldown.json', 'w') as file:
        json.dump(cds,file,indent=4)

class Reputation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def checkrep(self,ctx, user : discord.User=None):
        if not user:
            with open('./reps.json', 'r') as f:
                rep = json.load(f)
                avatarurl = ctx.message.author.avatar_url
                embed = discord.Embed(title=ctx.message.author.name + "#" + ctx.message.author.discriminator + "'s reputation points",timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=avatarurl)
                embed.add_field(name="Reputation points", value=rep[str(ctx.message.author.id)])
                await ctx.send(embed=embed)
        else:
            with open('./reps.json', 'r') as f:
                rep = json.load(f)
                avatarurl = user.avatar_url
                embed = discord.Embed(title=user.name + "#" + user.discriminator + "'s reputation points",timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=avatarurl)
                embed.add_field(name="Reputation points", value=rep[str(user.id)])
                await ctx.send(embed=embed)

    @commands.command()
    async def addrep(self,ctx,user: discord.User):
        if user.id == ctx.message.author.id:
            await ctx.send("Need to specify a different user to give a reputation point to!")
        else:
            with open('./cooldown.json', 'r') as f:
                cds = json.load(f)
            if cds[str(ctx.message.author.id)] == False:
                with open('./reps.json', 'r') as f:
                    rep = json.load(f)
                rep[str(user.id)] = rep[str(user.id)] + 1
                with open('./reps.json', 'w') as f:
                    json.dump(rep, f, indent=4)
                    await ctx.send(f"{ctx.message.author.mention} gave a reputation point to {user.mention}")
                cds[str(ctx.message.author.id)] = True
                with open('./cooldown.json', 'w') as file:
                    json.dump(cds,file,indent=4)
                self.bot.loop.create_task(timeouttask(ctx))
            else:
                await ctx.send(f"{ctx.message.author.mention}, your cooldown isn't off yet!")
    @addrep.error
    async def addrep_error(self,ctx,error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("You need to specify an user")
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def clearreps(self,ctx):
        guild = ctx.guild
        with open('./reps.json', 'r') as f:
            rep = json.load(f)
        with open('./reps.json', 'w') as file:
            for x in self.bot.guilds:
                gld = await self.bot.fetch_guild(x.id)
                async for member in gld.fetch_members(limit=1000):
                    if not member.bot:
                        rep[str(member.id)] = reps
            json.dump(rep,file,indent=4)
        with open('./cooldown.json', 'r') as f:
            cds = json.load(f)
        with open('./cooldown.json', 'w') as file:
            for x in self.bot.guilds:
                gld = await self.bot.fetch_guild(x.id)
                async for member in gld.fetch_members(limit=1000):
                    if not member.bot:
                        cds[str(member.id)] = False
            json.dump(cds,file,indent=4)

    @clearreps.error
    async def clearreps_error(self,error):
        if isinstance(error, NotOwner):
            pass


def setup(bot):
    bot.add_cog(Reputation(bot))