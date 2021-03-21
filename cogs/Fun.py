import discord
from discord.ext import commands
import random
from discord.ext import tasks



class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nigga(self, ctx):
        await ctx.reply('nigga', mention_author=False)

    @commands.command(pass_context = True)
    async def swag(self, ctx):
        text = str(random.randint(0, 100)) 
        text += '%'
        embed = discord.Embed(title = "Swag Meter", description  = (text), color = (0xa11cff))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['sav', 'serverav', 'avatarserver'])
    async def serveravatar(self, ctx):
        text = str(ctx.guild.name)
        text += " Server Avatar"
        mbed = discord.Embed(
            color=discord.Color(0xa11cff),
            title=(text)
        )
        mbed.set_image(url=f"{ctx.guild.icon_url}")
        await ctx.reply(embed=mbed, mention_author=False)

    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            color=discord.Color(0xa11cff),
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user: discord.Member):
        mbed = discord.Embed(
            color=discord.Color(0xa11cff),
            title=f"{user}"
        )
        mbed.set_image(url=f"{user.avatar_url}")
        await ctx.reply(embed=mbed, mention_author=False)

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            mbed = discord.Embed(
                color=discord.Color(0xa11cff),
                title=f"{ctx.author}"
            )
            mbed.set_image(url=f"{ctx.author.avatar_url}")
            await ctx.reply(embed=mbed, mention_author=False)

    def osu_keknigga(ctx):
        return ctx.guild.id == 820324203508269127

    @commands.command()
    @commands.check(osu_keknigga)
    async def gay(self, ctx):
        responses = ['twinh',
                     'Treuil',
                     'MQHX',
                     'Shadow',
                     'Tin',
                     'YouTu',
                     'Arlind',
                     'WalidESpagnol',
                    ]
        await ctx.reply(f'{random.choice(responses)} is gay', mention_author=False)

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f'Pong! {round(self.bot.latency * 1000)}ms', mention_author=False)

def setup(bot):
    bot.add_cog(Fun(bot))
