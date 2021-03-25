import asyncio

import discord
from discord.ext import commands


class ListenerBog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel.id != 746147917651509329:  # just joined channel other than the bog chat
            bog_chat = discord.utils.get(discord.guild.voice_channels, id = 746147917651509329)
            print(f"Found Bog Chat. {bog_chat.id}")

            joined_channel = await self.bot.join_voice_channel(bog_chat)
            player = joined_channel.create_ffmpeg_player('jackson_in_bog_chat.mp3', after = lambda: print(f"Told {member.name} that Jackson is in the Bog Chat."))
            player.start()

            while not player.is_done():
                await asyncio.sleep(1)

            player.stop()
            await joined_channel.disconnect()
