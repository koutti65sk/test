import discord
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/',intents = intents)


logchannel = 928951765867585536


@bot.event
async def on_ready():
    print('Ready!')
    channel = bot.get_channel(logchannel)
    await bot.send.channel('logined')

@bot.listen()
async def on_message(message):
    print('one')


bot.run(token)