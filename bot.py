import nextcord
from nextcord.ext import commands

from module_bog import ListenerBog
from module_bog_backup import ListenerBogBackup
from module_confessions import ListenerConfession
from module_dnd import ListenerDnD
from module_help import Help, description
from module_misc import ListenerMisc
from module_reaction_images import ReactionImages
from module_vote_to_kick import Kick
from secrets import key

intents = nextcord.Intents.default()

bot = commands.Bot(command_prefix = '!', description = description, intents = intents)
client = nextcord.Client()
bot.remove_command("help")


@bot.event
async def on_ready():
    print('Logged in as', bot.user.name, "(" + str(bot.user.id) + ")")
    print('------')


bot.add_cog(Kick(bot))
bot.add_cog(ReactionImages(bot))
bot.add_cog(ListenerMisc(bot))
bot.add_cog(ListenerDnD(bot))
bot.add_cog(Help(bot))
bot.add_cog(ListenerConfession(bot))
bot.add_cog(ListenerBog(bot))
bot.add_cog(ListenerBogBackup(bot))

bot.run(key)
