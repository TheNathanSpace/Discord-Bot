import json
import sqlite3
from datetime import datetime
from pathlib import Path

from nextcord import Guild, TextChannel, Message
from nextcord.ext import commands
from nextcord.ext.commands import Context


class SavedMessage:
    def __init__(self, message: Message):
        self.message_timestamp: float = message.created_at.timestamp()
        self.message_id: int = message.id
        self.channel_id: int = message.channel.id
        self.author_id: int = message.author.id
        attachment_list = message.attachments
        self.attachment_url_list = []
        if len(attachment_list) > 0:
            for attachment in attachment_list:
                self.attachment_url_list.append(attachment.url)

        self.message_text: str = "" + message.content

    async def get_reactions(self, message: Message):
        reactions = message.reactions
        new_reaction_list = {}
        reactions = message.reactions
        for reaction in reactions:
            if type(reaction.emoji) is str:
                name = reaction.emoji
                id = None
            else:
                id = reaction.emoji.id
                name = reaction.emoji.name

            users = await reaction.users().flatten()
            for user in users:
                if user.id not in new_reaction_list:
                    new_reaction_list[user.id] = []
                if id:
                    emoji_dict = {"name": name, "id": id}
                    new_reaction_list[user.id].append(emoji_dict)
                else:
                    new_reaction_list[user.id].append(name)

        self.reaction_dict = new_reaction_list


class ModuleAnalyze(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.latest_sender = None

    @commands.command()
    async def update_archive(self, context: Context):
        print(f"Started archiving messages from {context.guild.name}...")
        await context.message.delete()

        guild: Guild = context.guild
        text_channel_dict = {}
        for channel in guild.text_channels:
            text_channel_dict[channel.id] = None
        for thread in guild.threads:
            text_channel_dict[thread.id] = None

        self.create_database()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        channel_ids = cursor.execute('SELECT DISTINCT channel_id FROM messages;')
        for channel_id in channel_ids:
            channel_id = channel_id[0]
            if channel_id in text_channel_dict:
                text_channel_dict[channel_id] = True

        for channel_id in text_channel_dict:
            if text_channel_dict[channel_id] is not None:
                latest = cursor.execute('SELECT message_id FROM messages WHERE channel_id = ? ORDER BY message_timestamp DESC;', (channel_id,)).fetchone()
                text_channel_dict[channel_id] = latest[0]

        text_channel: TextChannel
        for text_channel_id in text_channel_dict:
            text_channel = guild.get_channel(text_channel_id)
            if text_channel is None:
                print(f"Error: Channel {text_channel_id} is null")
                continue

            print(f"On channel: {text_channel.name}")

            message_number = 0

            after = None
            if text_channel_dict[text_channel_id] is not None:
                message_id = text_channel_dict[text_channel_id]
                latest_message: Message = await text_channel.fetch_message(message_id)
                after = latest_message.created_at
                print("Getting all messages after " + after.date().strftime("%B %d, %G"))
            try:
                async for message in text_channel.history(limit = None, oldest_first = True, after = after):
                    message_number += 1
                    print(f"On message #{message_number}", end = "\r")
                    saved_message = SavedMessage(message)
                    while True:
                        try:
                            await saved_message.get_reactions(message)
                            break
                        except Exception as e:
                            print(f"Error getting reactions; retrying: {e}")

                    to_insert = (
                        saved_message.message_id, saved_message.channel_id, saved_message.author_id, saved_message.message_timestamp, json.dumps(saved_message.attachment_url_list), saved_message.message_text, json.dumps(saved_message.reaction_dict)
                    )
                    cursor.execute('INSERT INTO messages(message_id, channel_id, author_id, message_timestamp, attachment_url_list, message_text, reaction_list) VALUES(?,?,?,?,?,?,?) ON CONFLICT(message_id) DO NOTHING;', to_insert)

                    connection.commit()
            except:
                print(f"Error getting messages in channel {text_channel.name}. The bot probably doesn't have access to it.")

        print(f"Finished scraping messages from {context.guild.name}!")

    def create_database(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS messages(message_id integer PRIMARY KEY, channel_id integer, author_id integer, message_timestamp float, attachment_url_list text, message_text text, reaction_list text);')
        connection.commit()

    @commands.command()
    async def count_reactions(self, context: Context):
        print(f"Counting reactions...")
        await context.message.delete()

        self.create_database()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        all_rows = cursor.execute('SELECT reaction_list FROM messages WHERE reaction_list != ?;', ("{}",)).fetchall()
        user_reactions = {}
        for row in all_rows:
            reaction_dict = json.loads(row[0])
            for user in reaction_dict:
                for reaction in reaction_dict[user]:  # reaction: {"name": "uptrump_old", "id": 730559664625811486}
                    if user not in user_reactions:
                        user_reactions[user] = {}

                    reaction_name = None
                    if type(reaction) is dict:
                        reaction_name = reaction["name"]
                    else:
                        reaction_name = reaction

                    if reaction_name not in user_reactions[user]:
                        user_reactions[user][reaction_name] = 0

                    user_reactions[user][reaction_name] += 1

        new_dict = {}
        for user in user_reactions:
            try:
                username = await context.guild.fetch_member(user)
            except:
                username = "Unknown user"

            new_dict[f"{username} ({user})"] = dict(sorted(user_reactions[user].items(), key = lambda item: item[1], reverse = True))

        Path(f"reactions_{datetime.now().timestamp()}.json").write_text(json.dumps(new_dict, indent = 4, ensure_ascii = False), encoding = "utf8")
        print(f"Finished counting reactions!")

    # This fixes the older version of the database where the reactions hadn't been named
    @commands.command()
    async def fix_reactions(self, context: Context):
        await context.message.delete()
        print(f"Started fixing reactions in {context.guild.name}...")
        self.create_database()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        all_rows = cursor.execute('SELECT channel_id, message_id, reaction_list FROM messages WHERE reaction_list != ?;', ("{}",)).fetchall()
        row_num = 0
        for row in all_rows:
            row_num += 1
            channel_id = row[0]
            message_id = row[1]
            reaction_list = row[2]
            if "{\"name\":" in reaction_list:
                continue
            reaction_dict = json.loads(reaction_list)
            to_fix = False
            for user in reaction_dict:
                for reaction in reaction_dict[user]:
                    if not (isinstance(reaction, str) or isinstance(reaction, dict)):
                        to_fix = True
                        break
                if to_fix:
                    break

            if not to_fix:
                continue

            print(f"On row {row_num}", end = "\r")
            channel = await context.guild.fetch_channel(channel_id)
            message = await channel.fetch_message(message_id)
            new_reaction_list = {}
            reactions = message.reactions
            for reaction in reactions:
                if type(reaction.emoji) is str:
                    name = reaction.emoji
                    id = None
                else:
                    id = reaction.emoji.id
                    name = reaction.emoji.name

                users = await reaction.users().flatten()
                for user in users:
                    if user.id not in new_reaction_list:
                        new_reaction_list[user.id] = []
                    if id:
                        emoji_dict = {"name": name, "id": id}
                        new_reaction_list[user.id].append(emoji_dict)
                    else:
                        new_reaction_list[user.id].append(name)

            cursor.execute('UPDATE messages SET reaction_list = ? WHERE message_id = ?;', (json.dumps(new_reaction_list), message_id))
            connection.commit()

        print(f"Finished fixing emojis in {context.guild.name}!")
