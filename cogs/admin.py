from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
import discord
import datetime

class AdminCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self,ctx,limit : int):
        await ctx.channel.purge(limit=limit)

    @purge.error
    async def purge_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            embed = discord.Embed(title="Incorect use of `purge` command!",timestamp=datetime.datetime.utcnow(),color=discord.Colour.red())
            embed.add_field(name="Correct use of purge command", value="```..purge amount```")
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, user : discord.Member=None, *,args):
        _roles = []
        for x in user.roles:
            if not x.name == "@everyone":
                _roles.append(x.mention)
        roles = ", ".join(_roles)

        perms = []
        for x,y in user.permissions_in(ctx.channel):
            if y == True:
                perms.append(x)
        _permissions = ", ".join(perms)
        if user.guild_permissions.ban_members:
            await ctx.send("I can't ban him")
            await ctx.message.add_reaction("❌")
        else:
            embed = discord.Embed(title=f"{ctx.message.author} banned {user.name}#{user.discriminator}",timestamp=datetime.datetime.utcnow(), color=discord.Colour.purple())
            embed.add_field(name="Reason: ",value=f"```{args}```",inline=False)
            embed.add_field(name="Roles: ", value=f"{roles}",inline=False)
            embed.add_field(name="Permissions: ", value=f"```{_permissions}```")
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
            await ctx.guild.ban(user,reason=args)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            embed = discord.Embed(title="Incorect use of `ban` command!",timestamp=datetime.datetime.utcnow(),color=discord.Colour.red())
            embed.add_field(name="Correct use of ban command", value="```..ban user reason```")
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, user : discord.Member=None, *, args):
        _roles = []
        for x in user.roles:
            if not x.name == "@everyone":
                _roles.append(x.mention)
        roles = ", ".join(_roles)

        perms = []
        for x,y in user.permissions_in(ctx.channel):
            if y == True:
                perms.append(x)
        _permissions = ", ".join(perms)
        if user.guild_permissions.ban_members:
            await ctx.send("I can't kick him")
            await ctx.message.add_reaction("❌")
        else:
            embed = discord.Embed(title=f"{ctx.message.author} kicked {user.name}#{user.discriminator}",timestamp=datetime.datetime.utcnow(), color=discord.Colour.purple())
            embed.add_field(name="Reason: ",value=f"```{args}```",inline=False)
            embed.add_field(name="Roles: ", value=f"{roles}",inline=False)
            embed.add_field(name="Permissions: ", value=f"```{_permissions}```")
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
            await ctx.guild.kick(user,reason=args)

    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            embed = discord.Embed(title="Incorect use of `kick` command!",timestamp=datetime.datetime.utcnow(),color=discord.Colour.red())
            embed.add_field(name="Correct use of kick command", value="```..kick user reason```")

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,user:discord.User=None,*,args : str=None):
        try:
            await ctx.guild.unban(user,reason=args)
            embed = discord.Embed(title=f"{ctx.message.author} unbanned {user.name}#{user.discriminator}")
            embed.add_field(name="Reason: ", value=f"{args}")
            await ctx.send(embed=embed)
        except:
            await ctx.send("User is not banned")

    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,MissingRequiredArgument):
            embed = discord.Embed(title="Incorect use of `unban` command!",timestamp=datetime.datetime.utcnow(),color=discord.Colour.red())
            embed.add_field(name="Correct use of unban command", value="```..unban user reason(optional)```")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AdminCommands(bot))