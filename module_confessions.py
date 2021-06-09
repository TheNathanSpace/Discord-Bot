import json
import time
from datetime import datetime
from pathlib import Path

import discord
from discord.ext import commands


class ListenerConfession(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.latest_sender = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if int(message.channel.id) == int(788839489216315433):
            confessions_file = Path("confessions.txt")

            if not confessions_file.exists():
                confessions_file.touch()

            now_timestamp = time.time()
            offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)

            message_time = message.created_at
            message_time = message_time + offset

            jump_url = message.jump_url

            time_string = "[" + message_time.strftime("%b %d, %Y %H:%M:%S.%f") + "]"
            author_string = message.author.name

            prefix = f"{time_string} {author_string}: "
            empty_prefix = " " * len(prefix)

            attachment_list = message.attachments
            if len(attachment_list) > 0:
                attachment_url_list = []
                for attachment in attachment_list:
                    attachment_url = attachment.url
                    attachment_url_list.append(attachment_url)

                serialized_attachments = json.dumps(attachment_url_list)

                empty_prefix = " " * len(prefix)

            with confessions_file.open("a") as f:
                f.write(f"{prefix}{message.content}\n")

                # if len(embed_list) > 0:
                #     f.write(f"{empty_prefix}{serialized_embeds}\n")

                if len(attachment_list) > 0:
                    f.write(f"{empty_prefix}{serialized_attachments}\n")

            private_confessions_channel = self.bot.get_channel(819972744221163603)

            if len(message.content) > 0:
                content_to_send = "> " + message.content
            else:
                content_to_send = ""

            if len(attachment_list) > 0:
                if len(message.content) > 0:
                    content_to_send = content_to_send + "\n" + serialized_attachments
                else:
                    content_to_send = serialized_attachments

            new_author = False
            if self.latest_sender is None or self.latest_sender != message.author:
                author_string = f"**{author_string}:**\n"
                new_author = True
            else:
                author_string = ""

            if len(message.content) > 0 and new_author:
                content_to_send = f"{author_string} {jump_url}" + content_to_send
            elif len(message.content) > 0 and not new_author:
                content_to_send = content_to_send
            else:
                content_to_send = author_string + content_to_send

            self.latest_sender = message.author

            if len(message.embeds) > 0:
                embed_to_send = message.embeds[0]

                await private_confessions_channel.send(content = content_to_send, embed = embed_to_send)
            else:
                await private_confessions_channel.send(content = content_to_send)
