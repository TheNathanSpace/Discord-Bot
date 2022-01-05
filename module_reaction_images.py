import nextcord
from nextcord.ext import commands

image_dict = {"hitler": "https://i.imgur.com/CadlYk7.mp4", "cringe": "https://i.imgur.com/HYRgmzY.png", "cring": "https://i.imgur.com/HFr2wDu.png", "funny": "https://i.imgflip.com/3npccy.png", "beat": "https://i.imgur.com/WCBTQ71.png",
              "tyrant": "https://i.imgur.com/l702mF4.jpg", "madness": "https://i.imgur.com/xPtdCTa.png"}


class ReactionImages(commands.Cog, name = "Reaction Images"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cringe(self, ctx):
        """"The goose,  Mr. Holmes!  The goose,  sir!" he gasped."""
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["cringe"])
        await ctx.send(embed = e)

    @commands.command()
    async def cring(self, ctx):
        """"Th goose,  Mr. Holms!  Th goose,  sir!" h gaspd."""
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["cring"])
        await ctx.send(embed = e)

    @commands.command()
    async def funny(self, ctx):
        """" """
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["funny"])
        await ctx.send(embed = e)

    @commands.command(aliases = ['bat'])
    async def beat(self, ctx):
        """TOTALLY not radical, dude."""
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["beat"])
        await ctx.send(embed = e)

    @commands.command()
    async def tyrant(self, ctx):
        """I will burn like the heathen kings of old."""
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["tyrant"])
        await ctx.send(embed = e)

    @commands.command(aliases = ['madnss'])
    async def madness(self, ctx):
        """It's just... good business."""
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["madness"])
        await ctx.send(embed = e)

    @commands.command(aliases = ['hitlr'])
    async def hitler(self, ctx):
        """Don't be stupid, be a **smarty!**"""
        trigger = ctx.message
        await trigger.delete()
        try:
            myfile = nextcord.File("/home/nathan/Reaction-Image/THAT%27S%20OUR%20HITLER%20small.gif", filename = "image.gif")
            await ctx.send(file = myfile)
        except FileNotFoundError:
            myfile = nextcord.File("THAT'S OUR HITLER small.gif", filename = "image.gif")
            await ctx.send(file = myfile)
