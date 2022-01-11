import discord
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

intent = discord.Intents.all()

bot = commands.Bot(command_prefix='&',intents = intent)


bot.run(token)