import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

TOKEN = "MTA3Nzg5MTE5MDAzMDA3Mzg5Ng.GJRcVG.9kc0E3omEdS9stFZgbDMQc4fzRnoNV_6yyWTJw"

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=';', intents=intents)


@client.event
async def on_ready():
    print("Bot Online As: " + client.user.name + "#" + client.user.discriminator)


"""@client.event
async def on_message(message):
    # channel = client.get_channel(1030698526075785298)
    # await channel.send('testing')
    print(message.author, message.content, message.channel.id)


#     pass
"""

@client.command
async def hello(ctx):
    print("RUN")
    await ctx.channel.send_message("FUCK U")
    #channel1 = ctx.channel
    #channel = client.get_channel(921289830124642327)
    #await channel1.send(f'hello there {ctx.author.mention}')


keep_alive()
try:
    client.run(TOKEN)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')