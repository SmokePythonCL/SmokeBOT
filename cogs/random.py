import nextcord
from nextcord.ext import commands
import requests_html
import json
import random as r
from deep_translator import GoogleTranslator as t

#Random and useless commands.
class Random(commands.Cog,
             description='Sends a random thing related to the command.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Sends a random photo.')
    async def randomphoto(self, ctx):
        url = 'https://picsum.photos/5000/3333'
        session = requests_html.HTMLSession()
        photo = session.get(url)
        await ctx.send(photo.url)

    @commands.command(description='Sends a random photo of a fox.')
    async def fox(self, ctx):
        url = 'https://randomfox.ca/floof'
        session = requests_html.HTMLSession()
        photo = session.get(url)
        json_data = json.loads(photo.text)
        await ctx.send(json_data['image'])

    @commands.command(description='Sends a random photo of a duck.')
    async def duck(self, ctx):
        url = 'https://random-d.uk/api/v2/random'
        session = requests_html.HTMLSession()
        photo = session.get(url)
        json_data = json.loads(photo.text)
        await ctx.send(json_data['url'])

    @commands.command(description='Sends a random photo of a random animal.')
    async def animal(self, ctx):
        dog = 'https://dog.ceo/api/breeds/image/random'
        cat = 'https://aws.random.cat/meow'
        birb = 'https://some-random-api.ml/img/birb'
        duck = 'https://random-d.uk/api/v2/random'
        fox = 'https://randomfox.ca/floof'

        url = r.choice([dog, cat, birb, duck, fox])
        session = requests_html.HTMLSession()
        photo = session.get(url)
        json_data = json.loads(photo.text)
        if url == dog:
            await ctx.send(json_data['message'])
        elif url == cat:
            await ctx.send(json_data['file'])
        elif url == birb:
            await ctx.send(json_data['link'])
        elif url == duck:
            await ctx.send(json_data['url'])
        elif url == fox:
            await ctx.send(json_data['image'])

    #Sends a random fact translated to spanish.
    @commands.command(description="Sends a random useless fact. [These facts were translated from English, that's why some facts might not be understandable.]")
    async def dato(self, ctx):
      url = r.choice(['https://uselessfacts.jsph.pl/random.json?language=en', 'https://uselessfacts.jsph.pl/random.json?language=de'])
      session = requests_html.HTMLSession()
      fact = session.get(url)
      json_text = json.loads(fact.text)
      translated = t(source='auto', target='es').translate(text=json_text['text'])
      await ctx.send(translated)


def setup(bot):
    bot.add_cog(Random(bot))
