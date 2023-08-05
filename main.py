#IMPORTS
import os
import discord
import datetime
import asyncio
import sys
import platform
import datetime
from typing import Final

#FROM DISCORD
from discord.ext import commands, tasks


#INTENTS
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True


#DON'T GENERATE __PYCACHE__
sys.dont_write_bytecode = True


#DOTENV
TOKEN : Final[str] = os.environ['DISCORD_TOKEN']

#BOT CLASS
class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix="/", help_command=None, intents=intents)

    #ON_READY
    async def on_ready(self):
        timestamp = datetime.datetime.now()
        amount = len(bot.guilds)
        print("----------------------")
        print(f'The Flevarian Bot is online and in {amount} servers!')
        print('Ping: {0}ms'.format(round(bot.latency, 3)))
        print(f"API: {discord.__version__}")
        print(f"Python: {platform.python_version()}")
        print(timestamp.strftime("T: %d/%m/%Y %H:%M:%S\n----------------------"))

        #BOT LOOPS
        bot.loop.create_task(status_task())

    #LOAD COGS & SYNC SLASH COMMANDS
    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.startswith("__pycache__"):
                continue
            if filename.startswith("indev"):
                continue
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"----------------------\nLoaded {filename}")
            else:
                print(f"----------------------\nError loading {filename}")

        await self.tree.sync()
        print("----------------------")
        print("Synced Slash Commands")
        print("----------------------")


#DEFINE BOT
bot = Bot()

#LOAD COG COMMAND
@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.channel.send(f"Loaded **{extension}.py** successfully!")


#UNLOAD COG COMMAND
@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.channel.send(f"Unloaded **{extension}.py** successfully!")


#RELOAD COG COMMAND
@bot.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await bot.load_extension(f"cogs.{extension}")
    await ctx.channel.send(content=f"Reloaded **{extension}.py** successfully!")


#LOADINDEV COG COMMAND
@bot.command(hidden=True)
@commands.is_owner()
async def loadindev(ctx):
    for filename in os.listdir('./cogs/indev'):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.indev.{filename[:-3]}")
                await ctx.channel.send(f"Loaded **{filename}** successfully!")
                print(f"----------------------\nLoaded {filename}")
                await asyncio.sleep(1)


#UNLOADINDEV COG COMMAND
@bot.command(hidden=True)
@commands.is_owner()
async def unloadindev(ctx):
    for filename in os.listdir('./cogs/indev'):
            if filename.endswith(".py"):
                await bot.unload_extension(f"cogs.indev.{filename[:-3]}")
                await ctx.channel.send(f"Unloaded **{filename}** successfully!")
                print(f"----------------------\nLoaded {filename}")
                await asyncio.sleep(1)


#SHUTDOWN COMMAND
@bot.command(hidden=True)
@commands.is_owner()
async def shutdown(ctx):
    await ctx.channel.send("Shutting down...")
    await bot.close()


#BOT STATUS
@bot.event
async def status_task():
    amount = len(bot.guilds)
    while True:
        await bot.change_presence(activity=discord.Game(name="Prefix: /"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name="All hair Babis!"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name="Visit Flevaria sometime!"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name="beep boop"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name="Now supports Slash Commands!"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name=f"In {amount} servers!"))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(name="boop beep boop?"))
        await asyncio.sleep(120)

bot.run(TOKEN)
#os.environ.get() returns str | None, but .run accepts str (guessing that giving it none spits out an error)
#Typing check was giving me a headache about it, and os.environ[] fixes it, cause it returns str. Ciao!