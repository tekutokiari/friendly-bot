from discord import mentions
from discord.ext import commands
import discord
import asyncio

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def avatar(self,ctx, user : discord.User=None):
        if not user:
            await ctx.send(ctx.author.avatar_url)
        else:
            await ctx.send(user.avatar_url)
        
    @commands.command()
    async def bite(self,ctx,user: discord.Member=None):
        if not user:
            await ctx.send("You need to mention an user to bite!")
        else:
            embed = discord.Embed()
            embed.set_author(name="nom nom")
            embed.set_image(url='https://i.gifer.com/IDRX.gif')
            await ctx.send(f"{ctx.message.author.mention} chomped {user.mention}",embed=embed)

    @commands.command()
    async def satana(self,ctx,user:discord.Member=None):
        if not user:
            await ctx.send("You need to mention someone to exorcize")
        else:
            await ctx.send("Exorcizamus te, omnis immundus spiritus, omnis satanica potestas, omnis incursio infernalis adversarii, omnis legio, omnis congregatio et secta diabolica. Ergo, omnis legio diabolica, adiuramus te…cessa decipere humanas creaturas, eisque æternæ perditionìs venenum propinare…")
            await asyncio.sleep(0.5)
            await ctx.send("Vade, satana, inventor et magister omnis fallaciæ, hostis humanæ salutis…Humiliare sub potenti manu Dei; contremisce et effuge, invocato a nobis sancto et terribili nomine…quem inferi tremunt…Ab insidiis diaboli, libera nos, Domine.")
            await asyncio.sleep(0.5)
            await ctx.send("Ut Ecclesiam tuam secura tibi facias libertate servire, te rogamus, audi nos.")
            embed = discord.Embed()
            embed.set_image(url="https://minted-uk.com//wp-content//uploads//2018//10//28617_GoldenCross_r_web-910x910.jpg")
            await ctx.send(f"{ctx.message.author.mention} just exorcized {user.mention}",embed=embed)
def setup(bot):
    bot.add_cog(Fun(bot))