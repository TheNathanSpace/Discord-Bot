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
            voice = discord.utils.get(member.guild.voice_channels, id = 746147917651509329)

            joined_channel = await voice.connect()

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            voice.play(discord.FFmpegPCMAudio("jackson_in_bog_chat.mp3"))
            voice.volume = 100
            voice.is_playing()

            await joined_channel.disconnect()
