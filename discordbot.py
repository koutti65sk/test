import discord
from discord.ext import commands
import os

token = os.environ['DISCORD_BOT_TOKEN']

intent = discord.Intents.all()

bot = commands.Bot(command_prefix='&',intents = intent)


@bot.listen()
async def on_message_delete(message):
    if message.author.bot:
        return
    else:
        channel = bot.get_channel(dlelogchannel)
        sender_url = message.author.display_avatar
        embed = discord.Embed(
        title = "メッセージが削除されました。。",color = 0x4682B4
        )
        embed.set_author(
        name = "メッセージ削除ログ",icon_url = bot.user.avatar_url
        )
        embed.set_thumbnail(url = message.user.avatar_url)
        embed.add_field(name="チャンネル",value=message.channel.channel_mention,inline=False)
        embed.add_field(name="コンテンツ",value=message.content,inline=False)
        embed.add_field(name="削除者",value=sender_url,inline=False)
        if message.attachments:
            embed.add_field(name="ファイル",value=message.attachments)
        else:
            embed.add_field(name="ファイル",value="なし")
        await channel.send(embed = embed)
        return
    else:
        return













bot.run(token)
