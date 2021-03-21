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

    def Arlind_Server(ctx):
        return ctx.guild.id == 615615686622052354

    def osu_keknigga(ctx):
        return ctx.guild.id == 820324203508269127    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            pass

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    @commands.check(Arlind_Server)
    async def on_member_join(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='unverified')
        role2 = discord.utils.get(ctx.guild.roles, name="Donate for Elder (Bots)")
        if not ctx.bot:
            await ctx.add_roles(role)
        else:
            await ctx.add_roles(role2)

    @commands.Cog.listener()
    @commands.check(osu_keknigga)
    async def on_member_join(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='unverified')
        role2 = discord.utils.get(ctx.guild.roles, name="Bots")
        if not ctx.bot:
            await ctx.add_roles(role)
        else:
            await ctx.add_roles(role2)

def setup(bot):
    bot.add_cog(Events(bot))