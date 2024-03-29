import json
import random
from pathlib import Path

import nextcord
from nextcord.ext import commands
from nextcord.utils import get

image_dict = {"cringe": "https://i.imgur.com/HYRgmzY.png", "cring": "https://i.imgur.com/HFr2wDu.png", "funny": "https://i.imgflip.com/3npccy.png", "beat": "https://i.imgur.com/WCBTQ71.png",
              "tyrant": "https://i.imgur.com/l702mF4.jpg", "madness": "https://i.imgur.com/xPtdCTa.png", "a": "https://cdn.discordapp.com/attachments/885673393318404177/943333732532781076/unknown.png"}


class ReactionImages(commands.Cog, name = "Reaction Images"):
    def __init__(self, bot):
        self.bot = bot
        input_file = Path("food_gif_urls.txt")
        self.food_gifs = json.loads(input_file.read_text(encoding = "utf8"))

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

    @commands.command(aliases = [])
    async def a(self, ctx):
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        e.set_image(url = image_dict["a"])
        await ctx.send(embed = e)

    @commands.command(aliases = [])
    async def food(self, ctx):
        trigger = ctx.message
        await trigger.delete()
        e = nextcord.Embed()
        random_food = random.choice(self.food_gifs)
        e.set_image(url = random_food)
        await ctx.send(embed = e)
