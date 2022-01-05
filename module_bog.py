import asyncio
import os
from pathlib import Path

import discord
from discord import Guild, Message
from discord.ext import commands
from discord.ext.commands import Context
from discord.utils import get


class ListenerBog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def print_exception(self, e):
        if e:
            print(e)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.id == 762063323201536020:
            return

        if before.channel is None and after.channel.id != 746147917651509329:  # just joined channel other than the bog chat

            bog_chat = get(member.guild.voice_channels, id = 746147917651509329)

            if len(bog_chat.members) > 0:

                await asyncio.sleep(2)

                member_channel = after.channel

                voice = get(self.bot.voice_clients, guild = member.guild)

                if voice and voice.is_connected():
                    print("Already connected")
                    await voice.move_to(member_channel)
                else:
                    voice = await member_channel.connect()

                voice.play(discord.FFmpegPCMAudio("jackson_in_bog_chat.mp3"), after = lambda e: self.print_exception())

                while voice.is_playing():
                    await asyncio.sleep(1)

                await voice.disconnect()

    @commands.command(aliases = ['clan'])
    async def clean(self, ctx: Context, actual: bool = False):
        guild: Guild = ctx.guild
        bog_chat = get(guild.text_channels, id = 765299289516933151)
        messages = await bog_chat.history(limit = 200).flatten()
        message: Message

        delete_list = list()
        for message in messages:
            if message.content != "<:boggang:755109642966925392>":
                delete_list.append(message)

        embed = discord.Embed(
            colour = discord.Colour.dark_purple()
        )

        embed.add_field(name = "Number of messages to delete:", value = str(len(delete_list)), inline = True)
        embed.add_field(name = "Backup invite link:", value = "https://discord.gg/R7uQny8xzU", inline = True)

        embed.set_author(name = "Bog Chat Cleaner", icon_url = "https://i0.kym-cdn.com/entries/icons/facebook/000/019/601/smilelaugh.jpg", url = "https://www.youtube.com/watch?v=90hIAXlBGzY")
        await ctx.send(embed = embed)

        if not actual:
            value = ""
            for message in delete_list:
                value += "https://discord.com/channels/491392853801566226/765299289516933151/" + str(message.id)
                value += "\n"
            await ctx.send(value)
        else:
            for message in delete_list:
                await message.delete()

        trigger = ctx.message
        await trigger.delete()
