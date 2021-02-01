from discord.ext import commands
import discord
import datetime

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def userinfo(self,ctx,user: discord.Member=None):
        if not user:
            reg = ctx.author.created_at.__format__('%a, %d %b %Y %H:%M')
            rthen = ctx.author.created_at
            now = datetime.datetime.utcnow()
            rAge = now - rthen
            rdays = str(rAge).split(',', 1)
            jThen = ctx.author.joined_at
            jAge = now - jThen
            jdays = str(jAge).split(',', 1)
            _roles = []
            for x in ctx.author.roles:
                if not x.name == "@everyone":
                    _roles.append(x.mention)
            roles = ", ".join(_roles)
            _permissions = []
            for z,y in ctx.message.author.permissions_in(ctx.channel):
                if y == True:
                    _permissions.append(z)
            permissions = ", ".join(_permissions)
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(),color=discord.Colour.purple())
            embed.set_author(name=f"{ctx.author}",icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f"Sent by: {self.bot.user.name}#{self.bot.user.discriminator}",icon_url=ctx.author.avatar_url)
            embed.add_field(name="Status", value=f"```{ctx.author.status}```",inline=True)
            embed.add_field(name="Activity", value=f'```"{ctx.author.activity}"```',inline=True)
            embed.add_field(name="ID: ", value=f"```{ctx.author.id}```",inline=True)
            embed.add_field(name="Nickname: ",value=f"```{ctx.author.nick}```",inline=True)
            embed.add_field(name="Account created", value=f"```{reg} ({rdays[0]})```",inline=True)
            embed.add_field(name="Joined At: ",value=f"```{reg} ({jdays[0]})```",inline=True)
            embed.add_field(name="Roles: ", value=f"{roles}")
            embed.add_field(name="Permissions: ",value=f"```{permissions}```")
            await ctx.send(embed=embed)
        else:
            reg = user.created_at.__format__('%a, %d %b %Y %H:%M')
            rthen = user.created_at
            now = datetime.datetime.utcnow()
            rAge = now - rthen
            rdays = str(rAge).split(',', 1)
            jThen = user.joined_at
            jAge = now - jThen
            jdays = str(jAge).split(',', 1)
            _roles = []
            for x in user.roles:
                if not x.name == "@everyone":
                    _roles.append(x.mention)
            roles = ", ".join(_roles)
            _permissions = []
            for z,y in user.permissions_in(ctx.channel):
                if y == True:
                    _permissions.append(z)
            permissions = ", ".join(_permissions)
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(),color=discord.Colour.purple())
            embed.set_author(name=f"{user}",icon_url=user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text=f"Sent by: {self.bot.user}",icon_url=user.avatar_url)
            embed.add_field(name="Status", value=f"```{user.status}```",inline=True)
            embed.add_field(name="Activity", value=f'```"{user.activity.name}"```',inline=True)
            embed.add_field(name="ID: ", value=f"```{user.id}```",inline=True)
            embed.add_field(name="Nickname: ",value=f"```{user.nick}```",inline=True)
            embed.add_field(name="Account created", value=f"```{reg} ({rdays[0]})```",inline=True)
            embed.add_field(name="Joined At: ",value=f"```{reg} ({jdays[0]})```",inline=True)
            embed.add_field(name="Roles: ", value=f"{roles}")
            embed.add_field(name="Permissions: ",value=f"```{permissions}```")
            await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self,ctx):
        reg = ctx.guild.created_at.__format__('%a, %d %b %Y %H:%M')
        rthen = ctx.guild.created_at
        now = datetime.datetime.utcnow()
        rAge = now - rthen
        rdays = str(rAge).split(',', 1)
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(),color=discord.Colour.red())
        textchannelsnr = 0
        voicechannelsnr = 0
        for x in ctx.guild.text_channels:
            textchannelsnr = textchannelsnr + 1
        for y in ctx.guild.voice_channels:
            voicechannelsnr = voicechannelsnr + 1
        categoriesnr = 0
        for z in ctx.guild.categories:
            categoriesnr = categoriesnr + 1
        total=0
        humans=0
        bots=0
        for xy in ctx.guild.members:
            total = total + 1
            if xy.bot == True:
                bots=bots+1
            else:
                humans=humans+1
        roles = []
        for x in ctx.guild.roles:
            if not x.name == "@everyone": 
                roles.append(x.mention)
        _roles = ", ".join(roles)
        embed.set_author(name=f'"{ctx.guild.name.upper()}" Server Info',icon_url=f"{ctx.guild.icon_url}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.add_field(name="Owner: ", value=f"```{ctx.guild.owner}```",inline=True)
        embed.add_field(name="Region: ", value=f"```{ctx.guild.region}```",inline=True)
        embed.add_field(name="Created At: ", value=f"```{reg} ({rdays[0]})```",inline=True)
        embed.add_field(name="Guild ID: ", value=f"```{ctx.guild.id}```",inline=False)
        embed.add_field(name="Text Channels: ", value=f"```{textchannelsnr}```",inline=True)
        embed.add_field(name="Voice Channels: ", value=f"```{voicechannelsnr}```",inline=True)
        embed.add_field(name="Categories: ", value=f"```{categoriesnr}```")
        embed.add_field(name="Members: ", value=f"```{total} [Humans: {humans}, Bots: {bots}]```",inline=False)
        embed.add_field(name="Roles: ", value=f"{_roles}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))