import discord
import asyncio
from discord.ext import commands
 
class Administrator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        msg = await ctx.reply("ok", mention_author=False)
        await asyncio.sleep(3)
        await msg.delete()

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User):
        guild = ctx.guild
        mbed = discord.Embed(
            title = 'Success',
            descrition = f'{user} has been banned.'
        )
        await ctx.reply(embed=mbed, mention_author=False)
        await guild.ban(user=user)
         
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.User):
        guild = ctx.guild
        mbed = discord.Embed(
            title = 'Success',
            descrition = f'{user} has been kicked.'
        )
        await ctx.reply(embed=mbed, mention_author=False)
        await guild.kick(user=user)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User):
        guild = ctx.guild
        mbed = discord.Embed(
            title = 'Success',
            descrition = f'{user} has been unbanned.'
        )
        await ctx.reply(embed=mbed, mention_author=False)
        await guild.unban(user=user)

def setup(bot):
    bot.add_cog(Administrator(bot))