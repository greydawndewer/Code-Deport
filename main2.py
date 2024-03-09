import os
import discord
import logging
from discord.ext import commands
from keep_alive import keep_alive
import json

TOKEN = "MTA3Nzg5MTE5MDAzMDA3Mzg5Ng.GJRcVG.9kc0E3omEdS9stFZgbDMQc4fzRnoNV_6yyWTJw"
global channel_name
global my_client_id


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Greetings
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("HELLO")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("bye")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("MESSAGE")

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot has reconnected!')

    # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Uncomment line 26 for printing debug
        # await ctx.send(error)

        # Unknown command
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid Command!')

        # Bot does not have permission
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot Permission Missing!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')
        await ctx.message.delete()


# Gateway intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

# Bot prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or(';'),
                   description='A Simple Tutorial Bot',
                   intents=intents)

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Loading data from .env file

if __name__ == '__main__':
    # Load extension
    async def load_extensions():
        print("GONE")
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'commands.{filename[: -3]}')


async def setup(bot):
    await bot.add_cog(Settings(bot))


keep_alive()
try:
    bot.run(TOKEN, reconnect=True)
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
