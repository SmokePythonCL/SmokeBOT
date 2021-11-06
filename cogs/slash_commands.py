import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
import random as r
import requests_html
import json
from deep_translator import GoogleTranslator as t
import datetime

guilds = []

#Commands with the slash discord function.
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
                      name="test",
                      description='Just a test',
                      guild_ids=guilds)
                      
    async def _test(self, ctx: SlashContext):
        await ctx.send('Test completed!')

    @cog_ext.cog_slash(
                      name='ping',
                      description='Latency of the bot.',
                      guild_ids=guilds)
    
    async def _ping(self, ctx: SlashContext):
      await ctx.send(f'The bot latency is {round(self.bot.latency * 1000)} ms')

    @cog_ext.cog_slash(
                      name='fact',
                      description="Sends a random useless fact.",
                      guild_ids=guilds)
    
    async def _fact(self, ctx):
      url = r.choice(['https://uselessfacts.jsph.pl/random.json?language=en', 'https://uselessfacts.jsph.pl/random.json?language=de'])
      session = requests_html.HTMLSession()
      fact = session.get(url)
      json_text = json.loads(fact.text)
      translated = t(source='auto', target='es').translate(text=json_text['text'])
      await ctx.send(translated)


    @cog_ext.cog_slash(
                      name="stats",
                      description='Show stats of the server.',
                      guild_ids=guilds)
                      
    async def stats(self, ctx):
        embed = discord.Embed(timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name='Members', value=f'{ctx.guild.member_count}', inline=True)
        embed.add_field(name='Created in', value=f'{ctx.guild.created_at.day} - {ctx.guild.created_at.month} - '
                                                f'{ctx.guild.created_at.year}', inline=True)

        await ctx.send(embed=embed)

    @cog_ext.cog_slash(
                      name="clear",
                      description='[Administrator] Clear the submitted amount of messages.',
                      guild_ids=guilds,
                      default_permission=False,
                      permissions= 
                        [
                          {
                           :
                          create_permission(, SlashCommandPermissionType.ROLE, True)
                    	    },
                          {
                           : 
                          create_permission(, SlashCommandPermissionType.ROLE, True)
                          }
                        ]
                      )
                          
    async def clear(self, ctx, quantity:int):
        await ctx.channel.purge(limit=quantity)
        await ctx.send(f'The last {quantity} messages were eliminated.')

def setup(bot):
    bot.add_cog(Slash(bot))