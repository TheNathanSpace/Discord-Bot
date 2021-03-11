from pathlib import Path

from discord.ext import commands


class ListenerConfession(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if int(message.channel.id) == int(788839489216315433):
            confessions_file = Path("confessions.txt")

            if not confessions_file.exists():
                confessions_file.touch()

            time_string = "[" + message.created_at.strftime("%b %d, %Y %H:%M:%S.%f") + "]"
            author_string = message.author.name
            with confessions_file.open("a") as f:
                f.write(f"{time_string} {author_string}: {message.content}\n")
