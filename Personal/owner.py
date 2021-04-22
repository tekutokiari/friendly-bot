from discord.ext import commands
import discord
import io
import traceback
import textwrap
from contextlib import redirect_stdout
import asyncio

def cleanup_code(content):
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
    return content.strip('` \n')

class OwnerCommands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(aliases=['eval', 'ev'], hidden=True)
    @commands.is_owner()
    async def _eval(self,ctx, *, body):
        _last_result = None
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': _last_result
        }
        env.update(globals())
        body = cleanup_code(body)
        stdout = io.StringIO()
        to_compile = f'async def func():\n{textwrap.indent(body, " ")}'
        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass
        if ret is None:
            # pyright: reportUnboundVariable=false
            if value:
                await ctx.send(f'```py\n{value}\n```')
            else:
                _last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')
    @_eval.error
    async def _eval_error(self,ctx,error):
        if isinstance(error,UnboundLocalError):
            pass

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reply(self,ctx, user : discord.User ,*,args):
        await user.send(args)
        await ctx.message.add_reaction('\u2705')

    @reply.error
    async def reply_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            pass

    @commands.command(hidden=True)
    @commands.is_owner()
    async def purgedms(self,ctx):
        ch = await self.bot.fetch_channel('798192971346477097')
        messages = await ch.history(limit=100).flatten()
        for x in messages:
            if x.author.id == self.bot.user.id:
                await x.delete()
                await asyncio.sleep(0.15)
                
def setup(bot):
    bot.add_cog(OwnerCommands(bot))