from discord.ext import commands
from requests import get


class ListenerMisc(commands.Cog):
    def __init__(self, bot, c):
        self.bot = bot
        self.c = c

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):  # 168223477105426432
        if member.id == 168223477105426432 and before.channel is None and after.channel is not None:
            await member.edit(nick = "Mr. Active Apparently")
        if member.id == 168223477105426432 and before.channel is not None and after.channel is None:
            await member.edit(nick = "Mr. Inactive Apparently")

    @commands.command()
    async def java(self, ctx):
        await ctx.message.delete()
        await ctx.send("mE AND MY COHORT UPDATING OUR JAVA VERSIONS TO THE LATEST VERSION OF JAVA 8 FOR LOWER THAN 1.12 AND THE LATEST VERSION OF JAVA 14 FOR 1.12+\n\nhttps://gist.github.com/jellysquid3/8a7b21e57f47f5711eb5697e282e502e")

    @commands.command(aliases = ['address', 'ipaddress', 'server'])
    async def ip(self, ctx):
        trigger = ctx.message
        await trigger.delete()

        ip = get('https://api.ipify.org').text

        await ctx.send(f"Minigames server IP address: `{ip}:20202`")

    @commands.command(aliases = [])
    async def goat(self, ctx):
        """Goat"""
        trigger = ctx.message
        await trigger.delete()
        await ctx.send("!clear")
        await ctx.send("!play https://www.youtube.com/playlist?list=PLgzlUkIE7GetXYU0e3GiVISdaJPa_fWlH")
        await ctx.send("!shuffle")

    @commands.command(aliases = [])
    async def techno(self, ctx):
        """TECHNO UNION TECHNO UNION"""
        trigger = ctx.message
        await trigger.delete()
        await ctx.send("!clear")
        await ctx.send("!play https://www.youtube.com/playlist?list=PLgzlUkIE7GetEvgEWRDaUDGbH0u_0IA7i")
        await ctx.send("!shuffle")