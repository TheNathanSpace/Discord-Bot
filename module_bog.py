import asyncio

import discord
from discord.ext import commands


class ListenerBog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel.id != 746147917651509329:  # just joined channel other than the bog chat
            bog_chat = discord.utils.get(member.guild.voice_channels, id = 746147917651509329)

            joined_channel = await bog_chat.connect()
            self.bot.voice_clients[0].play(discord.FFmpegPCMAudio('jackson_in_bog_chat.mp3'))
            await joined_channel.disconnect()
