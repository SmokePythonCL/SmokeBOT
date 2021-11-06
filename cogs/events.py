import nextcord
from nextcord.ext import commands


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Set the presence in discord to Streaming.
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=nextcord.Streaming(name='',
                                                                  url='',
                                                                  platform='',
                                                                  twitch_name=''))
        
        print(f'Connected!\n{self.bot.user}')

    #Checks every message
    @commands.Cog.listener('on_message')
    async def the_message(self, message):
        if message.author == self.bot.user:
            return

        print(f'Message from {message.author}: {message.content} with ID: {message.id}')

        #Sends a response to a message in a DM channel.
        if message.author != self.bot.user and message.channel.type.name == 'private':
            content = ""
            await message.channel.send(content)
        
        #Sends a message when an specified user sends a messages.
        if str(message.author) == '':
            await message.channel.send('')
        
    #Create a custom welcome with an embed message.
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            embed = nextcord.Embed(title=f'{member.display_name}',
                                  description='')

            if member.avatar_url:
                embed.set_thumbnail(url=f'{member.avatar_url}')
            elif not member.avatar_url:
                embed.set_thumbnail(url=f'{member.default_avatar_url}')

            await guild.system_channel.send(embed=embed)

    #Checks a deleted message in a specified channel.
    @commands.Cog.listener('on_raw_message_delete')
    async def deleted_message(self, payload):
      
      if payload.channel_id == channel:
        print(f'Message deleted from {payload.cached_message.author}: {payload.cached_message.content} with ID {payload.message_id}.')

def setup(bot):
    bot.add_cog(Events(bot))
