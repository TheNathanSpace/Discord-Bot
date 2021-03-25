import asyncio
import os
from pathlib import Path

import discord
from discord.ext import commands
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
