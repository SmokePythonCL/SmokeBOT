import discord
import os
import json
from discord.ext import commands
from variables import discord_token #Using another file for privacy.
from discord_slash import SlashCommand


# Read the prefix for the servers.
def get_prefix(bot, message):
    with open('../DiscordBOT/json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


intents = discord.Intents(members=True, messages=True, guilds=True)
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True)


# Command to load a Cog (only administrators).
@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


# Command to load a Cog (only administrators).
@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


# Command to load a Cog (only administrators).
@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    


# Add the server to the prefixes list.
@bot.event
async def on_guild_join(guild):
    with open('../DiscordBOT/json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '?'

    with open('../DiscordBOT/json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


# Remove the server from the prefixes list.
@bot.event
async def on_guild_remove(guild):
    with open('../DiscordBOT/json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('../DiscordBOT/json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


# Command to change prefix (Only administrators).
@bot.command()
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix):
    with open('../DiscordBOT/json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('../DiscordBOT/json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    
    await ctx.send(f'Your prefix was successfully change to {prefix}')

#Load the cogs.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    bot.run(discord_token)