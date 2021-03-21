import os
import discord
import json
import asyncio
import random
import datetime
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.utils import get

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot  

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            pass

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

def setup(bot):
    bot.add_cog(Events(bot))