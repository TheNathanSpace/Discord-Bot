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
            voice = discord.utils.get(member.guild.voice_channels, id = after.channel.id)

            joined_channel = await voice.connect()

            # voice = get(bot.voice_clients, guild = ctx.guild)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            joined_channel.play(discord.FFmpegPCMAudio("jackson_in_bog_chat.mp3"))
            joined_channel.volume = 100
            joined_channel.is_playing()

            await joined_channel.disconnect()
