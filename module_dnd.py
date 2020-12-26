import math
import re

import discord
from discord.ext import commands


class ListenerDnD(commands.Cog):
    def __init__(self, bot, c):
        self.bot = bot
        self.c = c

    @commands.command()
    async def prices(self, ctx):
        """"DnD prices"""
        embed = discord.Embed(
            colour = discord.Colour.dark_purple()
        )

        prices_list = {"Korath fuel": "100(V) / 1 dL", "Nutrient paste": "2(V) / 1 L (Okella Station)\n 4(V) / 1 L (Black Market)", "O2 canister": "10(V) / 1, refill 1(V)"}

        for price in prices_list:
            embed.add_field(name = price, value = prices_list[price], inline = False)

        embed.set_author(name = "Prices", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")

        await ctx.send(embed = embed)

    @commands.command()
    async def travel(self, ctx, light_years, size_class, days, do_fuel = False):
        """"Life is a highway..."""
        try:
            if do_fuel:
                days_taken = (float(size_class) / math.sqrt((float(days) / float(light_years))))
                await ctx.send("It's gonna take " + str(round(days_taken, 3)) + " days")
            else:
                fuel = (float(light_years) * ((float(size_class) / float(days)) ** 2))
                await ctx.send("You're gonna need " + str(round(fuel, 3)) + " dL")
        except ValueError:
            await ctx.send("*am i a joke to you*")

    @commands.command()
    async def food(self, ctx, people, food_dl):
        try:
            days = (float(food_dl) / float(people))
            await ctx.send(f"That's gonna last you {round(days, 3)} days")
        except ValueError:
            await ctx.send("*am i a joke to you*")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.id == 762063323201536020:
            channel = message.channel

            if "Bruh imagine going somewhere with different exchange rates" in message.content:
                await channel.send("bruh")

            if "Hail Dirko" in message.content:
                await channel.send("Hail Dirko")

            found_vb = re.findall("(\d+\.?\d*) *(\((V|v)\)|V|v){1}", message.content)

            for full_match in found_vb:
                amount = full_match[0]

                amount = float(amount)
                gold = amount * 5 / 4
                await channel.send(f"{str(amount)}(V) = " + str("{:,}".format(round(gold, 3))) + "gp")

            found_gp = re.findall("(\d+\.?\d*) *(gp){1}", message.content)

            for full_match in found_gp:
                amount = full_match[0]

                amount = float(amount)
                v_bucks = amount * 4 / 5
                await channel.send(f"{str(amount)}gp = " + str("{:,}".format(round(v_bucks, 3))) + "(V))")
