import asyncio
import os

import discord
from discord.ext import commands
from discord.utils import get


class ListenerBog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.id == 762063323201536020:
            return

        if before.channel is None and after.channel.id != 746147917651509329:  # just joined channel other than the bog chat
            print("Okay")
            await asyncio.sleep(2)

            member_channel = after.channel
            print(member_channel.id)

            voice = get(self.bot.voice_clients, guild = member.guild)

            if voice and voice.is_connected():
                print("Already connected")
                await voice.move_to(member_channel)
            else:
                voice = await member_channel.connect()

            # voice = get(bot.voice_clients, guild = ctx.guild)

            print("Trying to play audio")
            voice.play(discord.FFmpegPCMAudio("jackson_in_bog_chat.mp3"), after = lambda e: print('done', e))
            voice.volume = 100

            print(f"Playing: {voice.is_playing()}")

            await voice.disconnect()
