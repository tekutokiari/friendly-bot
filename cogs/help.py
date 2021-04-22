from os import name
from typing import Text
from discord.ext import commands
import discord
import datetime

class HelpCommand(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(case_insensitive=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            admincog = self.bot.get_cog('AdminCommands')
            cmds = admincog.get_commands()
            admincommands = []
            for x in cmds:
                admincommands.append(x.name)
            _admincommands = ", ".join(admincommands)

            funcog = self.bot.get_cog('Fun')
            cmds2 = funcog.get_commands()
            funcommands = []
            for y in cmds2:
                funcommands.append(y.name)
            _funcommands = ", ".join(funcommands)

            reputationcog = self.bot.get_cog('Reputation')
            cmds3 = reputationcog.get_commands()
            repcommands = []
            for z in cmds3:
                if z.hidden == False:
                    repcommands.append(z.name)
            _repcommands = ", ".join(repcommands)

            infocog = self.bot.get_cog('Info')
            cmds4 = infocog.get_commands()
            infocmds = []
            for xx in cmds4:
                if xx.hidden == False:
                    infocmds.append(xx.name)
            _infocmds = ", ".join(infocmds)
            embed = discord.Embed(title="Help commands", timestamp=datetime.datetime.utcnow(),color=discord.Colour.red())
            embed.add_field(name=f"{admincog.qualified_name}", value=f"```{_admincommands}```",inline=False)
            embed.add_field(name=f"{funcog.qualified_name}", value=f"```{_funcommands}```",inline=False)
            embed.add_field(name=f"{reputationcog.qualified_name}",value=f"```{_repcommands}```",inline=False)
            embed.add_field(name=f"{infocog.qualified_name}", value=f"```{_infocmds}```",inline=False)
            embed.set_footer(text=f"For more info do: {ctx.prefix}help 'command'",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)

    
    @help.command()
    async def purge(self,ctx):
        embed = discord.Embed(title="```purge help command```", timestamp=datetime.datetime.utcnow(),color=discord.Colour.purple())
        embed.set_author(name="Purge an amount of messages in this channel")
        embed.add_field(name="Usage:", value=f"```{ctx.prefix}purge 'number'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ",value="```MANAGE_MESSAGES```")
        embed.set_footer(text=f"Requester: {ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def ban(self,ctx):
        embed = discord.Embed(title="```ban help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Ban someone from the server.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}ban 'member' (reason)```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```BAN_MEMBERS```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def kick(self,ctx):
        embed = discord.Embed(title="```kick help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Kick someone from the server.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}kick 'member' (reason)```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```KICK_MEMBERS```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def unban(self,ctx):
        embed = discord.Embed(title="```unban help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Unban someone's ID.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}unban 'member' (reason)```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```BAN_MEMBERS```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def avatar(self,ctx):
        embed = discord.Embed(title="```avatar help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Mention someone to see their avatar.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}avatar 'user'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def bite(self,ctx):
        embed = discord.Embed(title="```bite help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Mention someone to bite them.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}bite 'user'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def satana(self,ctx):
        embed = discord.Embed(title="```satana help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Mention someone to exorcize  them.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}satana 'user'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def checkrep(self, ctx):
        embed = discord.Embed(title="```checkrep help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Check how many reputation points you or someone else have.")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}checkrep no user/'user'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def addrep(self, ctx):
        embed = discord.Embed(title="```addrep help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Give a reputation point to someone of your choice")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}addrep 'user'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def userinfo(self,ctx):
        embed = discord.Embed(title="```userinfo help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Shows info about you or someone you mention")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}userinfo no user/'user'```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    @help.command()
    async def serverinfo(self,ctx):
        embed = discord.Embed(title="```serverinfo help command```", timestamp=datetime.datetime.utcnow(),color = discord.Colour.purple())
        embed.set_author(name="Shows info about the server")
        embed.add_field(name="Usage: ", value=f"```{ctx.prefix}serverinfo```")
        embed.add_field(name="NSFW: ", value="```No```")
        embed.add_field(name="Permissions: ", value="```NONE```")
        embed.set_footer(text=f"Requester:{ctx.message.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(HelpCommand(bot))