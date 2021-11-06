import nextcord
from nextcord.ext import commands

#Some errors handling.
class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            print(f'{error}')

        elif isinstance(error, commands.errors.MissingPermissions):
            print(f'{error}')


def setup(bot):
    bot.add_cog(Errors(bot))