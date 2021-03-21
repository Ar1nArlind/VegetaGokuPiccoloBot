import discord
from discord.ext import commands
import random

class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def verifyDeeServerTest(ctx):
        return ctx.guild.id == 805007738458865685

    def Arlind_Server(ctx):
        return ctx.guild.id == 615615686622052354

    def osu_keknigga(ctx):
        return ctx.guild.id == 820324203508269127

    @commands.command()
    @commands.check(Arlind_Server)
    async def coc(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Clash of Clans")

        if role in user.roles:
            msg = await ctx.reply("Attempting to remove role from {}".format(user), mention_author=False)

            try:
                await user.remove_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' removed!".format(role))
        else:
            msg = await ctx.reply("Attempting to add role to {}".format(user), mention_author=False)

            try:
                await user.add_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' added!".format(role))

        await asyncio.sleep(3)

    @commands.command()
    @commands.check(Arlind_Server)
    async def addict(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="drug addict")

        if role in user.roles:
            msg = await ctx.reply("Attempting to remove role from {}".format(user), mention_author=False)

            try:
                await user.remove_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' removed!".format(role))
        else:
            msg = await ctx.reply("Attempting to add role to {}".format(user), mention_author=False)

            try:
                await user.add_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' added!".format(role))

        await asyncio.sleep(3)

    @commands.command()
    @commands.check(Arlind_Server)
    async def miku(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Hatsune Miku Specialist")

        if role in user.roles:
            msg = await ctx.reply("Attempting to remove role from {}".format(user), mention_author=False)

            try:
                await user.remove_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' removed!".format(role))
        else:
            msg = await ctx.reply("Attempting to add role to {}".format(user), mention_author=False)

            try:
                await user.add_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' added!".format(role))

        await asyncio.sleep(3)

    @commands.command()
    async def nsfw(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="NSFW")

        if role in user.roles:
            msg = await ctx.reply("Attempting to remove role from {}".format(user), mention_author=False)

            try:
                await user.remove_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' removed!".format(role))
        else:
            msg = await ctx.reply("Attempting to add role to {}".format(user), mention_author=False)

            try:
                await user.add_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' added!".format(role))

        await asyncio.sleep(3)

    @commands.command()
    async def islam(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="islam")

        if role in user.roles:
            msg = await ctx.reply("Attempting to remove role from {}".format(user), mention_author=False)

            try:
                await user.remove_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' removed!".format(role))
        else:
            msg = await ctx.reply("Attempting to add role to {}".format(user), mention_author=False)

            try:
                await user.add_roles(role)
            except:
                await msg.edit(content="There was an error running this command!")
            else:
                await msg.edit(content="Role '{}' added!".format(role))

        await asyncio.sleep(3)

    @commands.command()
    async def verify(self, ctx):

        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Member")
        role2 = discord.utils.get(ctx.guild.roles, name="unverified")

        if role2 in user.roles:
            await user.remove_roles(role2)
            await user.add_roles(role)
            await ctx.reply("Successfully verified {}".format(user), mention_author=False)

        await asyncio.sleep(3)


def setup(bot):
    bot.add_cog(Roles(bot))