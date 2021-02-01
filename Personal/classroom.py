import discord
from discord.ext import commands
import datetime
import time
import discord
import asyncio
from main import bot

francezalink = 'https://classroom.google.com/u/1/c/MTcxNTA2OTMyODAz'
francezalinkmeet = 'https://meet.google.com/lookup/ee6p3s2any'
istorielink = 'https://classroom.google.com/u/1/c/MTg3NjQ3NjQ1Mzc2'
istorielinkmeet = 'https://meet.google.com/lookup/enj6ax2a5w'
englezalink = 'https://classroom.google.com/u/1/c/MTYxNDQxMDkxMTQ5'
englezalinkmeet = 'https://meet.google.com/lookup/dhc772vdym'
romanalink = 'https://classroom.google.com/u/1/c/MTgwNDIwNDE1ODAy'
romanalinkmeet = 'https://meet.google.com/lookup/cgraj6sw7e'
economielink = 'https://classroom.google.com/u/1/c/MTc2MDYyNzkyMzEx'
economielinkmeet = 'https://meet.google.com/lookup/fsa3ybb45f'
chimielink = 'https://classroom.google.com/u/1/c/MTY5Mjc2NjQ3OTA2'
sportlink = 'https://classroom.google.com/u/1/c/MTc2MTY5MjI4MTQ2'
sportlinkmeet = 'https://meet.google.com/lookup/bpejb6cv5c'
infolink = 'https://classroom.google.com/u/1/c/MTc2MzkxMDIwMjM4'
infolinkmeet = 'https://meet.google.com/lookup/fds237fofl'
dirigentielink = 'https://classroom.google.com/u/1/c/MTc2MTcwODg2MTg3'
dirigentielinkmeet = 'https://meet.google.com/lookup/fvwdovp4ln'
handicapatalink = 'https://classroom.google.com/u/1/c/MTc2Mzk4MzgzNzQz'
biologielink = 'https://classroom.google.com/u/1/c/MTQ1MzA5NTYzMjE0'
biologielinkmeet = 'https://meet.google.com/lookup/cdjs2fzhxx'
mateoptionallink = 'https://classroom.google.com/u/1/c/MTY0NDYwMDk2MzU0'
mateoptionallinkmeet = 'https://meet.google.com/lookup/dym5bzlmhd'
religielink = 'https://classroom.google.com/u/1/c/MTY0ODEwMzc2NjA0'
matelink = 'https://classroom.google.com/u/1/c/MTY0NzI1MzQyODgz'
geografielink = 'https://classroom.google.com/u/1/c/OTMxMzY1NTM3MDha'
fizicalink = 'https://classroom.google.com/u/1/c/NTYyMTI5NDE3MzFa'

async def oretask():
    zi = datetime.datetime.today().strftime('%A')
    trimis = False
    while True:
        ora = datetime.datetime.today().hour
        minute = datetime.datetime.today().minute
        print(minute)
        while ora >= 13 and ora <= 18:
            if zi == 'Monday':
                if ora == 13 and minute == 50 and trimis == False:
                    channel = await bot.fetch_channel('798250365903962122')
                    embedvar = discord.Embed(title="Istorie ",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Istorie Link: ", value=istorielink,inline=False)
                    embedvar.add_field(name="Istorie Link meet: ", value=istorielinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Iancu Ionut")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)   
                if ora == 14 and minute == 40 and trimis == False:
                    channel = await bot.fetch_channel('798250365903962122')
                    embedvar = discord.Embed(title="Informatica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Informatica Link: ", value=infolink,inline=False)
                    embedvar.add_field(name="Istorie Link meet: ", value=infolinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Constantin-Daniel Pietris")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 15 and minute == 30 and trimis == False:
                    channel = await bot.fetch_channel('798250365903962122')
                    embedvar = discord.Embed(title="Informatica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Informatica Link: ", value=infolink,inline=False)
                    embedvar.add_field(name="Informatica Link meet: ", value=infolinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Constantin-Daniel Pietris")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 16 and minute == 20 and trimis == False:
                    channel = await bot.fetch_channel('798250365903962122')
                    embedvar = discord.Embed(title="Religie",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Religie Link: ", value=religielink,inline=False)
                    embedvar.set_footer(text="Profesor: Nitoi Mirela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 17 and minute == 10 and trimis == False:
                    channel = await bot.fetch_channel('798250365903962122')
                    embedvar = discord.Embed(title="Franceza",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Franceza Link: ", value=francezalink,inline=False)
                    embedvar.add_field(name="Franceza Link meet: ", value=francezalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Patrulescu Clarida")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 18 and minute == 00 and trimis == False:
                    channel = await bot.fetch_channel('798250365903962122')
                    embedvar = discord.Embed(title="Franceza",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Franceza Link: ", value=francezalink,inline=False)
                    embedvar.add_field(name="Franceza Link meet: ", value=francezalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Patrulescu Clarida")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)            
            if zi == 'Tuesday':
                if ora == 13 and minute == 50 and trimis == False:
                    channel = await bot.fetch_channel('798250380050825246')
                    embedvar = discord.Embed(title="Matematica Optional ",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Matematica Optional Link: ", value=mateoptionallink,inline=False)
                    embedvar.add_field(name="Matematica Optional Link meet: ", value=mateoptionallinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Rizea Ioana")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)   
                if ora == 14 and minute == 40 and trimis == False:
                    channel = await bot.fetch_channel('798250380050825246')
                    embedvar = discord.Embed(title="Geografie",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Geografie Link: ", value=geografielink,inline=False)
                    embedvar.set_footer(text="Profesor: Datcu Paula")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 15 and minute == 30 and trimis == False:
                    channel = await bot.fetch_channel('798250380050825246')
                    embedvar = discord.Embed(title="Fizica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Fizica Link: ", value=fizicalink,inline=False)
                    embedvar.set_footer(text="Profesor: Anghel Daniela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 16 and minute == 20 and trimis == False:
                    channel = await bot.fetch_channel('798250380050825246')
                    embedvar = discord.Embed(title="Fizica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Fizica Link: ", value=fizicalink,inline=False)
                    embedvar.set_footer(text="Profesor: Anghel Daniela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 17 and minute == 10 and trimis == False:
                    channel = await bot.fetch_channel('798250380050825246')
                    embedvar = discord.Embed(title="Informatica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Informatica Link: ", value=infolink,inline=False)
                    embedvar.add_field(name="Informatica Link meet: ", value=infolinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Constantin-Daniel Pietris")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 18 and minute == 00 and trimis == False:
                    channel = await bot.fetch_channel('798250380050825246')
                    embedvar = discord.Embed(title="Informatica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Informatica Link: ", value=infolink,inline=False)
                    embedvar.add_field(name="Informatica Link meet: ", value=infolinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Constantin-Daniel Pietris")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar) 
            if zi == 'Wednesday':
                if ora == 13 and minute == 40 and trimis == False:
                    channel = await bot.fetch_channel('798250389513830420')
                    embedvar = discord.Embed(title="Lb. Engleza",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Lb. Engleza Link: ", value=englezalink,inline=False)
                    embedvar.add_field(name="Lb. Engleza Link meet: ", value=englezalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Cazan Daniela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 14 and minute == 40 and trimis == False:
                    channel = await bot.fetch_channel('798250389513830420')
                    embedvar = discord.Embed(title="Lb. Engleza",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Lb. Engleza Link: ", value=englezalink,inline=False)
                    embedvar.add_field(name="Lb. Engleza Link meet: ", value=englezalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Cazan Daniela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 15 and minute == 30 and trimis == False:
                    channel = await bot.fetch_channel('798250389513830420')
                    embedvar = discord.Embed(title="Biologie",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Biologie Link: ", value=biologielink,inline=False)
                    embedvar.add_field(name="Biologie Link meet: ", value=biologielinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Pitu Iuliana")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 16 and minute == 20 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Matematica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Matematica Link: ", value=matelink,inline=False)
                    embedvar.set_footer(text="Profesor: Vasile Mirela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 17 and minute == 10 and trimis == False:
                    channel = await bot.fetch_channel('798250389513830420')
                    embedvar = discord.Embed(title="Matematica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Matematica Link: ", value=matelink,inline=False)
                    embedvar.set_footer(text="Profesor: Vasile Mirela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
            if zi == 'Thursday':
                if ora == 13 and minute == 50 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Educatie Fizica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Educatie Fizica Link: ", value=sportlink,inline=False)
                    embedvar.add_field(name="Educatie Fizica Link meet: ", value=sportlinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Radulescu Mihaela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 14 and minute == 40 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Lb. Romana",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Lb. Romana Link: ", value=romanalink,inline=False)
                    embedvar.add_field(name="Lb. Romana Link meet: ", value=romanalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Serban Anca")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)               
                if ora == 15 and minute == 30 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Chimie",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Chimie Link: ", value=chimielink,inline=False)
                    embedvar.set_footer(text="Profesor: Butan Luminita")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)               
                if ora == 16 and minute == 20 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Matematica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Matematica Link: ", value=matelink,inline=False)
                    embedvar.set_footer(text="Profesor: Vasile Mirela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)              
                if ora == 17 and minute == 10 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Matematica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Matematica Link: ", value=matelink,inline=False)
                    embedvar.set_footer(text="Profesor: Vasile Mirela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
                if ora == 18 and minute == 0 and trimis == False:
                    channel = await bot.fetch_channel('798250398719803392')
                    embedvar = discord.Embed(title="Baze de date",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Baze de date Link: ", value=handicapatalink,inline=False)
                    embedvar.set_footer(text="Profesor: Ioan Cristina")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)
            if zi == 'Friday':
                if ora == 14 and minute == 40 and trimis == False:
                    channel = await bot.fetch_channel('798250406698156112')
                    embedvar = discord.Embed(title="Romana",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Romana Link: ", value=romanalink,inline=False)
                    embedvar.add_field(name="Romana Link meet: ", value=romanalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Serban Anca")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)               
                if ora == 15 and minute == 30 and trimis == False:
                    channel = await bot.fetch_channel('798250406698156112')
                    embedvar = discord.Embed(title="Romana",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Romana Link: ", value=romanalink,inline=False)
                    embedvar.add_field(name="Romana Link meet: ", value=romanalinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Serban Anca")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)              
                if ora == 16 and minute == 20 and trimis == False:
                    channel = await bot.fetch_channel('798250406698156112')
                    embedvar = discord.Embed(title="Economie",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Economie Link: ", value=economielink,inline=False)
                    embedvar.add_field(name="Economie Link meet: ", value=economielinkmeet,inline=False)
                    embedvar.set_footer(text="Profesor: Deaconu Florin")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)             
                if ora == 17 and minute == 10 and trimis == False:
                    channel = await bot.fetch_channel('798250406698156112')
                    embedvar = discord.Embed(title="Fizica",
                    colour=discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Fizica Link: ", value=fizicalink,inline=False)
                    embedvar.set_footer(text="Profesor: Anghel Daniela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar)    
                if ora == 18 and minute == 0 and trimis == False:
                    channel = await bot.fetch_channel('798250406698156112')
                    embedvar = discord.Embed(title="Fizica",
                    colour= discord.Colour(0xe74c3c))
                    embedvar.add_field(name="Fizica Link: ", value=fizicalink,inline=False)
                    embedvar.set_footer(text="Profesor: Anghel Daniela")
                    await channel.send("@everyone")
                    await channel.send(embed=embedvar) 
            break
        await asyncio.sleep(60)

class Classroom(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    @commands.is_owner()
    async def startore(self,ctx):
        pornit = False
        if datetime.datetime.today().second != 0 and pornit == False:
            await asyncio.sleep(60 - datetime.datetime.today().second)
            self.bot.loop.create_task(oretask())
            pornit = True
        
    @startore.error
    async def startore_error(self, ctx,error):
        if isinstance(error, commands.NotOwner):
            pass
        else:
            raise error
def setup(bot):
    bot.add_cog(Classroom(bot))