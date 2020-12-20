import asyncio
import random

import discord
from discord.ext import commands


class Kick(commands.Cog, name = "Kick (coming soon?)"):
    def __init__(self, bot):
        self.bot = bot

    async def kick_from_voice(self, member, ctx):
        if member != 235088799074484224:
            await member.move_to(None)

    @commands.command()
    async def kick(self, ctx, user_to_kick):

        if user_to_kick == "[user]":
            try:
                member = 363465027283320835
                await member.move_to(None)
                return
            except:
                await ctx.send("hm")

        """Vote to kick?"""
        trigger = ctx.message
        await trigger.delete()

        user_calling = trigger.author

        user_to_kick = user_to_kick.replace("<", "")
        user_to_kick = user_to_kick.replace(">", "")
        user_to_kick = user_to_kick.replace("!", "")
        user_to_kick = user_to_kick.replace("@", "")

        user = self.bot.get_user(int(user_to_kick))
        mention_string = user.mention

        embed = discord.Embed(
            colour = discord.Colour.dark_purple(),
            description = "Vote started by " + trigger.author.display_name + " to kick " + mention_string
        )

        embed.add_field(name = "Yes", value = ":white_check_mark:", inline = True)
        embed.add_field(name = "No", value = ":x:", inline = True)

        seconds_remaining = 5
        embed.insert_field_at(
            index = 2,
            name = 'Seconds remaining:',
            value = str(seconds_remaining),
            inline = False
        )

        embed.set_author(name = "Vote to kick?", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")

        kick_message = await ctx.send(embed = embed)

        await kick_message.add_reaction("✅")
        await kick_message.add_reaction("❌")

        while seconds_remaining > -1:
            embed.remove_field(index = 2)
            embed.insert_field_at(
                index = 2,
                name = 'Seconds remaining:',
                value = str(seconds_remaining),
                inline = False
            )

            await kick_message.edit(embed = embed)
            await asyncio.sleep(1)

            seconds_remaining -= 1

        kick_message = await ctx.fetch_message(kick_message.id)
        reactions_list = kick_message.reactions
        yes = -1
        no = -1
        for reaction in reactions_list:
            emoji = reaction.emoji
            if emoji == "✅":
                yes += reaction.count
            if emoji == "❌":
                no += reaction.count

        embed.remove_field(index = 0)
        embed.insert_field_at(index = 0, name = "Yes", value = ":white_check_mark:  " + str(yes), inline = True)

        embed.remove_field(index = 1)
        embed.insert_field_at(index = 1, name = "No", value = ":x:  " + str(no), inline = True)

        if yes > no:
            new_embed = discord.Embed(
                colour = discord.Colour.from_rgb(120, 178, 91),
                description = "Vote started by " + trigger.author.display_name + " to kick " + mention_string
            )
            new_embed.set_author(name = "Vote Results", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")
            new_embed.insert_field_at(index = 0, name = "Yes", value = ":white_check_mark:  " + str(yes), inline = True)
            new_embed.insert_field_at(index = 1, name = "No", value = ":x:  " + str(no), inline = True)

            embed.insert_field_at(
                index = 3,
                name = 'Vote result:',
                value = "Pass!",
                inline = False
            )
            new_embed.insert_field_at(
                index = 3,
                name = 'Vote result:',
                value = "Pass!",
                inline = False
            )

        else:
            new_embed = discord.Embed(
                colour = discord.Colour.from_rgb(219, 47, 63),
                description = "Vote started by " + trigger.author.display_name + " to kick " + mention_string
            )
            new_embed.set_author(name = "Vote Results", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")
            new_embed.insert_field_at(index = 0, name = "No", value = ":x:  " + str(no), inline = True)
            new_embed.insert_field_at(index = 1, name = "Yes", value = ":white_check_mark:  " + str(yes), inline = True)

            embed.insert_field_at(
                index = 3,
                name = 'Vote result:',
                value = "Fail!",
                inline = False
            )
            new_embed.insert_field_at(
                index = 3,
                name = 'Vote result:',
                value = "Fail!",
                inline = False
            )

        await kick_message.edit(embed = embed)
        await ctx.send(embed = new_embed)

        if yes > no:
            vc_list = ctx.guild.voice_channels
            for channel in vc_list:
                members = channel.voice_states.keys()
                for member in members:
                    if member == user.id:
                        random_chance = random.random()

                        if member == 235088799074484224:
                            random_chance = 0.8
                            mention_string = user_calling.mention
                            await ctx.send(mention_string + " lol u wish")

                        if random_chance > 0.9:
                            member = random.choice(list(members))
                            member = await ctx.message.guild.fetch_member(int(member))
                            await self.kick_from_voice(member, ctx)

                        elif (random_chance > 0.7) and (random_chance <= 0.9):
                            member = await ctx.message.guild.fetch_member(user_calling.id)
                            await self.kick_from_voice(member, ctx)

                        else:
                            member = await ctx.message.guild.fetch_member(int(member))
                            await self.kick_from_voice(member, ctx)
