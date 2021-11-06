import asyncio
import datetime
import nextcord
from nextcord.ext import commands

#Custom commands with prefixes.
class Comandos(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='For test the bot.')
    async def test(self, ctx):
        print('Test completed')
        await ctx.send('Test completed')

    @commands.command(description='Show stats of the server.')
    async def stats(self, ctx):
        embed = nextcord.Embed(timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name='Members', value=f'{ctx.guild.member_count}', inline=True)
        embed.add_field(name='Created in', value=f'{ctx.guild.created_at.day} - {ctx.guild.created_at.month} - '
                                                f'{ctx.guild.created_at.year}', inline=True)

        await ctx.send(embed=embed)

    @commands.command(description='Check the ping of the bot.')
    async def ping(self, ctx):
        await ctx.send(f'The bot latency is {round(self.bot.latency * 1000)} ms')

    @commands.command(description='[Administrator] Clear the submitted amount of messages (By default 5).')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'The last {amount} messages were eliminated.')

    #Error handling for bad argument in the last command.
    @clear.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.BadArgument):
            await ctx.send('Bad argument given.')
            

def setup(bot):
    bot.add_cog(Comandos(bot))
