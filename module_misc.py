import re

import pytz as pytz
from nextcord import Message, PartialMessageable
from nextcord.ext import commands
from requests import get


class ListenerMisc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(aliases = [])
    async def impeach(self, ctx):
        trigger = ctx.message
        await trigger.delete()
        await ctx.send("""IM IMPEACHING YOU, DONALD!:sob::wave:

██]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]] 10% complete…..

████]]]]]]]]]]]]]]]]]]]]]]]]]]] 35% complete….

███████]]]]]]]]]]]]]]]] 60% complete….

███████████] 99% complete…..

:no_entry_sign:ERROR!:no_entry_sign: :flag_ru:legitimate:flag_ru: presidents are irreplaceable :ballot_box: i could never delete you donald! :ballot_box: send this to ten other :briefcase:delegates:necktie: who give you :ballot_box_with_check:️votes:ballot_box_with_check:️ or never get jobs back from :flag_cn:china:flag_cn: again:x::x::construction_worker::factory::x::x: If you get 0 back: low-energy :no_entry_sign::no_entry_sign::turtle: 3 back: you’re bigly :top::frog: 5 back: you’re YUGE:tangerine::department_store::dollar: 10+ back: make america great again :star_and_crescent::taco::passport_control::no_entry::construction::statue_of_liberty::fireworks::flag_us:""")

    @commands.command(aliases = [])
    async def timestamp(self, ctx, message_id):
        trigger = ctx.message
        await trigger.delete()

        try:
            msg = await ctx.fetch_message(message_id)

            timezone = pytz.timezone("America/Denver")
            created_at = msg.created_at

            await ctx.send(f"Message `{str(message_id)}` created at {created_at.astimezone(timezone).strftime('%Y-%m-%d %H:%M:%S.%f %Z')}")
        except:
            await ctx.send("ur mum lol")

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        dm_channel = message.author.dm_channel
        if dm_channel is None:
            try:
                dm_channel = await message.author.create_dm()
            except:
                pass

        dm_channel = dm_channel.id

        if message.channel.id == dm_channel:  # dm only
            if message.author.id == 285538805728149504:
                matched = re.match("\[([0-9]*)\] (.*)", message.content)
                if matched is not None:
                    channel: PartialMessageable = self.bot.get_channel(int(matched.group(1)))
                    to_send = matched.group(2)
                    await channel.send(content = to_send)
