import os
import discord
import json
import asyncio
import random
import datetime
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.utils import get

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

def get_prefix(bot,message):
    with open('src/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix, case_insensitive=True, intents = intents)

def osu_keknigga(ctx):
    return ctx.guild.id == 704417229747388526


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.reply(f'Cog Loaded', mention_author=False)

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.reply(f'Cog Unloaded', mention_author=False)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.reply(f'Cog Reloaded', mention_author=False)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_guild_join(guild):
    with open('src/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '$'

    with open('src/prefixes.json', 'w') as f:
        json.dump(prefixes,f,indent=4)

@bot.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix):
    with open('src/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('src/prefixes.json', 'w') as f:
        json.dump(prefixes,f,indent=4)

    await ctx.send(f'The prefix was changed to {prefix}')

bot.run('Token')
