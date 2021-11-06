import nextcord
from nextcord.ext import commands
from nextcord.utils import find

#When the bots joins a server, it's sends a default notification in general.
class Notifications(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      general = find(lambda x: x.name == 'general',  guild.text_channels)

      if general and general.permissions_for(guild.me).send_messages:
        embed=nextcord.Embed(title="Welcome to ", description="The default prefix is ? ")
        embed.set_thumbnail(url="")
        embed.add_field(name="If you want to change the prefix use", value="?changeprefix", inline=False)
        embed.add_field(name="?help", value="To see the commands.", inline=False)
        embed.set_footer(text="?help")
        await general.send(embed=embed)

def setup(bot):
    bot.add_cog(Notifications(bot))
