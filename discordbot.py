import discord
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='&',intents = intents)


bot.run(token)