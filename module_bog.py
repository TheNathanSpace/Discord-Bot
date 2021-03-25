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
        if before.channel is None and after.channel.id != 746147917651509329:  # just joined channel other than the bog chat
            await asyncio.sleep(2)

            member_channel = member.voice.channel

            voice = get(self.bot.voice_clients, guild = member.guild)

            if voice and voice.is_connected():
                print("Already connected")
                await voice.move_to(member_channel)
            else:
                if voice:
                    voice_true = True
                else:
                    voice_true = False

                if voice.is_connected():
                    connected = True
                else:
                    connected = False

                print(f"Not connected. Voice: {voice_true}. Connected: {connected}.")

                voice = await member_channel.connect()

            # voice = get(bot.voice_clients, guild = ctx.guild)

            voice.play(discord.FFmpegPCMAudio("jackson_in_bog_chat.mp3"))
            voice.volume = 100
            voice.is_playing()

            await voice.disconnect()
