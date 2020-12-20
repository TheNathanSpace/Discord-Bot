import discord
from discord.ext import commands

from module_dnd import ListenerDnD
from module_help import Help
from module_misc import ListenerMisc
from module_reaction_images import ReactionImages
from module_vote_to_kick import Kick
from secrets import key

intents = discord.Intents.default()

bot = commands.Bot(command_prefix = '!', description = description, intents = intents)
client = discord.Client()
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, "(" + str(bot.user.id) + ")")
    print('------')


bot.add_cog(Kick(bot))
bot.add_cog(ReactionImages(bot))
bot.add_cog(ListenerMisc(bot, client))
bot.add_cog(ListenerDnD(bot, client))
bot.add_cog(Help(bot))

bot.run(key)
