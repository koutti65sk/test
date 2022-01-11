import discord
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/',intents = intents)


logchannel = 928951765867585536


async def great():
    channel = bot.get_channel(logchannel)
    await channel.send('logined')
    return

@bot.event
async def on_ready():
    print('Ready!')
    await great()
    return

@bot.listen()
async def on_message(message):
    print('one')
    return

bot.run(token)