import discord
from discord.ext import commands

description_reaction = {"!cringe": "\"The goose,  Mr. Holmes!  The goose,  sir!\" he gasped.", "!funny": "COMEDY ACHIEVED", "!beat": "TOTALLY not radical, dude.", "!tyrant": "I will burn like the heathen kings of old.",
                        "!madness": "It's just... good business.", "!hitler": "Don't be stupid, be a **smarty!**"}

description_dnd = {"!travel": "`!travel` `<light years>` `<size class>` `<days>`", "!travel (fuel)": "`!travel` `<light years>` `<size class>` `<fuel>` `true`", "!prices": "Display prices of space gear",
                   "!food": "`!food` `<number of people>` `<dL of food>`", "Currency Conversion": "Type the amount in chat, like `3000(V)` or `125gp`"}

description_utility = {"!kick [user]": "Vote to kick?", "!server": "Get the current minigames server IP address", "!java": "lol"}

description_help = {"!helpreaction": "Reaction images", "!helpdnd": "D&D functionality", "!helputility": "Other utility commands", "!help": "You already know  👉 😎 👉"}

description = '''Uh oh Watson, looks like somebody posted CRINGE!'''


class Help(commands.Cog, name = "Util Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["hlp"])
    async def help(self, ctx):
        """You already know 👉😎👉"""
        # trigger = ctx.message
        # await trigger.delete()

        embed = discord.Embed(
            colour = discord.Colour.dark_purple(),
            description = description
        )

        for desc in description_help:
            embed.add_field(name = desc, value = description_help[desc], inline = False)

        embed.set_author(name = "Help", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")

        await ctx.send(embed = embed)

    @commands.command(aliases = ['reaction'])
    async def helpreaction(self, ctx):
        """You already know 👉😎👉"""
        # trigger = ctx.message
        # await trigger.delete()

        embed = discord.Embed(
            colour = discord.Colour.dark_purple(),
            description = description
        )

        for desc in description_reaction:
            embed.add_field(name = desc, value = description_reaction[desc], inline = False)

        embed.set_author(name = "Help", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")

        await ctx.send(embed = embed)

    @commands.command(aliases = ['dndhelp'])
    async def helpdnd(self, ctx):
        """You already know 👉😎👉"""
        # trigger = ctx.message
        # await trigger.delete()

        embed = discord.Embed(
            colour = discord.Colour.dark_purple()
        )

        for desc in description_dnd:
            embed.add_field(name = desc, value = description_dnd[desc], inline = False)

        embed.set_author(name = "DnD Help", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")

        await ctx.send(embed = embed)

    @commands.command(aliases = [])
    async def helputility(self, ctx):
        """You already know 👉😎👉"""

        embed = discord.Embed(
            colour = discord.Colour.dark_purple()
        )

        for desc in description_utility:
            embed.add_field(name = desc, value = description_utility[desc], inline = False)

        embed.set_author(name = "DnD Help", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")

        await ctx.send(embed = embed)

    @commands.command(name = "supersecretadmincommandthatonlynathanknowsaboutpassword:scurvylegsmcgee")
    async def secret(self, ctx):
        """Spooooooky :O"""
        trigger = ctx.message
        await trigger.delete()

        await ctx.send("Spooooooooky :O\nhttps://www.youtube.com/watch?v=90hIAXlBGzY")
