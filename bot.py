import os
import discord
import time
import asyncio
import datetime
import random
import aiohttp

from discord import Guild, activity, Member, TextChannel, User

from discord.ext import commands, tasks
from discord.ext.commands import Bot, has_permissions, has_role, has_any_role, MissingPermissions, BadArgument
from discord.utils import get

from datetime import datetime
from itertools import cycle
from pretty_help import DefaultMenu, PrettyHelp

from webserver import keep_alive


intents = discord.Intents.all()
intents.members = True

players = {}

menu = DefaultMenu(page_left="◀", page_right="▶", remove="❌")
ending_note = "TimeBot Help Menu" 
no_category="Commands"

bot = commands.Bot(command_prefix='-', help_command=PrettyHelp(menu=menu, ending_note=ending_note, color=0xb40000, no_category=no_category, show_index=False, sort_commands=True, dm_help=True), intents=intents)

amount = 0

#BOT ONLINE PRINT

@bot.event
async def on_ready():
    timestamp = datetime.now()

    print("-------------------")
    print('TimeBot is online!')
    print('Ping: {0}ms'.format(round(bot.latency, 3)))
    print("-------------------")

    bot.loop.create_task(status_task())

# BOT COMMAND NOT FOUND ERROR

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("The command you entered doesn't exist!", delete_after=5)


#BOT CHANGE PRESENCE

@bot.event
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(name="MPAMPHS IS MY HERO"))





#BOT.LISTEN - 1

@bot.listen('on_message')
async def f(message):
    if message.author == bot.user:
        return

    elif 'f in chat' in message.content.lower():
        await message.channel.send('F')


#BOT.LISTEN - 2

@bot.listen('on_message')
async def f(message):
    if message.author == bot.user:
        return

    elif 'timebot best bot' in message.content.lower():
        await message.channel.send('STRAIGHT FACTS')


#BOT.LISTEN - 3

@bot.listen('on_message')
async def f(message):
    if message.author == bot.user:
        return

    elif 'i love this bot' in message.content.lower():
        await message.channel.send("Love you too homie.")


#BOT.LISTEN - 4

@bot.listen('on_message')
async def f(message):
    if message.author == bot.user:
        return

    elif 'the magic of timebot' in message.content.lower():
        await message.channel.send("✨Magic✨")



#ANTI-SPAM BOT.LISTEN

#TBD


#ANTI-DISCORD SERVER ADS BOT.LISTEN

@bot.listen('on_message')
async def antiserverads(message):
    if message.author.id == (640145015800332328) or (833995282773049344):
        return

    elif "discord.gg" in message.content.lower():
        await message.delete()
        await message.channel.send("Don't advertise your server!")


#MEME COMMAND

@bot.command(pass_context=True)
async def meme(ctx):
    subreddit = ['https://www.reddit.com/r/dankmemes/new.json?sort=hot',
                'https://www.reddit.com/r/memes/new.json?sort=hot',
                'https://www.reddit.com/r/meme/new.json?sort=hot',
                'https://www.reddit.com/r/me_irl/new.json?sort=hot']

    random_post = res['data']['children'] [random.randint(0, 30)]['data']['url']
    image_url = random_post["data"]["url"]
    post_title = random_post["data"]["title"]

    async with aiohttp.ClientSession() as clientsesh:
        async with clientsesh.get(random.choice(subreddit)) as reddit:
            res = await reddit.json()
            embed = discord.Embed(title="MEME", description="")
            embed.set_image(url=image_url)
            await ctx.channel.send(embed=embed)


#MUTE COMMAND

@bot.command(help="Mutes a user. For use until timeout command is added.", hidden=True)
@has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member, *, reason=None):
    logs_channel = bot.get_channel(847617704474312714)
    mute_role = discord.utils.get(ctx.guild.roles, id=937364278892171305)
    member_role = discord.utils.get(ctx.guild.roles, id=847613347716530227)
    await member.add_roles(mute_role, reason=reason)
    await member.remove_roles(member_role, reason=reason)
    await ctx.channel.send(f'Muted {member.mention}\n-Reason: {reason}', delete_after=10)
    await logs_channel.send(f'Muted {member.mention}\n-Reason: {reason}\n-Command issued by: {ctx.message.author.mention}')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#UNMUTE COMMAND

@bot.command(help="Unmutes a user.", hidden=True)
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    logs_channel = bot.get_channel(847617704474312714)
    mute_role = discord.utils.get(ctx.guild.roles, id=937364278892171305)
    member_role = discord.utils.get(ctx.guild.roles, id=847613347716530227)
    await member.remove_roles(mute_role)
    await member.add_roles(member_role)
    await ctx.channel.send(f'Unmuted {member.mention}', delete_after=10)
    await logs_channel.send(f'Unmuted {member.mention}\n-Command issued by: {ctx.message.author.mention}')

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#CLEAR COMMAND 

@bot.command(help="Clears given number of messages", hidden=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    if amount==1:
        await ctx.channel.send('Deleted 1 message', delete_after=3)
    else:
        await ctx.channel.send(f'Deleted {amount} messages', delete_after=3)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#ADMIN/MODERATOR ALERT COMMAND

@bot.command(help="Alerts all administrators", hidden=True)
@has_role(846864506617724958)
async def alert(ctx):
    admin_role = discord.utils.get(ctx.guild.roles, id=846864605052403732)
    await ctx.channel.send(f'Alert! All {admin_role.mention} personnel report to the Staff Chat ASAP!')

@alert.error
async def alert_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#LATENCY COMMAND

@bot.command(help="Shows latency")
async def ping(ctx):
    await ctx.channel.send("Ping/Latency: {0} ms".format(round(bot.latency, 3)))


#FUN COMMAND 1

@bot.command(help="")
async def warhammer(ctx):
    await ctx.channel.send("ONCE THE WARHAMMER DROPS...")
    await asyncio.sleep(1)
    await ctx.channel.send("...YOU SHALL BE FLATTENED")
    await asyncio.sleep(1)
    await ctx.channel.send("-random flat earther")


#KICK COMMAND

@bot.command(help="Kicks a user.", hidden=True)
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    logs_channel = bot.get_channel(847617704474312714)
    await member.kick(reason=reason)
    await ctx.channel.send(f'Kicked {member.mention}\n-Reason: {reason}', delete_after=10)
    await logs_channel.send(f'Kicked {member.mention}\n-Reason: {reason}\n-Command issued by:{ctx.message.author.mention}')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#BAN COMMAND

@bot.command(help="Bans a user.", hidden=True)
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    logs_channel = bot.get_channel(847617704474312714)
    await member.ban(reason=reason)
    await ctx.channel.send(f'Banned {member.mention}\n-Reason: {reason}')
    await ctx.channel.send("https://imgur.com/a/e3g5W37")
    await logs_channel.send(f'Banned {member.mention}\n-Reason: {reason}\n-Command issued by:{ctx.message.author.mention}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#UNBAN COMMAND

@bot.command(help='Unbans a banned user.', hidden=True)
@has_permissions(ban_members=True)
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send(f"{ctx.message.author.mention}, you don't have the permission to do that!", delete_after=5)


#REPORT COMMAND
@bot.command(help="Sends a report to the staff team of the server. This can be used for reporting users and/or problems with the bot/server.")
async def report(ctx, member : discord.Member, *, reason=None):
    reports_channel = bot.get_channel(937072708703907861)
    moderator_role = discord.utils.get(ctx.guild.roles, id=846864605052403732)

    if reason is None:
        await ctx.channel.send("Please provide a reason/description!")
    else:
        await ctx.channel.send(f'User {member.mention} was reported.', delete_after=10)
        await reports_channel.send(f'**REPORT**\n\nReported User: {member.mention} (ID: {member.id})\nReport by: {ctx.author.mention} (ID: {ctx.author.id})\n\nReason: {reason}')


#INFO COMMAND

@bot.command(help='Gives info about the server.')
async def serverinfo(ctx):
    embed = discord.Embed(title="Timeless28 Discord Server", description="", color=0xb40000)
    embed.add_field(name="Server Created At:", value=ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
    embed.add_field(name="Server Owner:", value=ctx.guild.owner, inline=False)
    embed.add_field(name="Role Count:", value=len(ctx.guild.roles), inline=False)
    embed.add_field(name="Category Count:", value=len(ctx.guild.categories), inline=False)
    embed.add_field(name="Channel Count:", value=len(ctx.guild.channels), inline=False)
    embed.add_field(name="Booster Status:", value=ctx.guild.premium_subscription_count, inline=False)
    await ctx.channel.send(embed=embed)


#WHOIS COMMAND

@bot.command(help="Shows info about a specified user", aliases=["userinfo"])
async def whois(ctx, member: discord.Member = None):
    if member == None: 
        member = ctx.message.author

    embed = discord.Embed(color=0xb40000, timestamp=ctx.message.created_at, title=f"Who dis?")
    embed.set_thumbnail(url=member.avatar_url)
    
    embed.add_field(name="Name", value=member.name)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nickname:", value=member.display_name)
    embed.add_field(name="Status", value=member.status)
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%d/%m/%Y %H:%M:%S"))
    embed.add_field(name="Joined Server On:", value=(member.joined_at.strftime("%d/%m/%Y %H:%M:%S")))

    await ctx.send(embed=embed)


#discord.Color.dark_red()
#0xb40000


#SOCIALS COMMAND

@bot.command(help="Lists TimelessTTV's social media accounts. pls follow me btw")
async def socials(ctx):
    await ctx.channel.send("-TikTok: <https://tiktok.com/@timelessttv>\n\n-YouTube: <https://www.youtube.com/channel/UC_E94MhLA5QDCefWXLqW33A>\n\n-Instagram: <https://instagram.com/timeless.ttv>\n\n-Twitter: <https://twitter.com/Timeless_TTV>\n\n-Twitch: <https://twitch.tv/timelessttv>\n\n-Subreddit: <https://www.reddit.com/r/TimelessTTV>")


#STUPID METER COMMAND

@bot.command(help="Measures how stupid you (or a specified user) are!")
async def stupid(ctx, member : discord.Member = None):
    percentage = (random.randint(0, 100))

#Checks if author is Revehound, then if author is aTPB, else picks percentage for message.author
    if member == None:
        
        if ctx.message.author.id == (725050369339687045):
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"You are 69% stupid!")

        elif ctx.message.author.id == (931613722567385138):
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"You are 100% stupid!")

        else:
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"You are {percentage}% stupid!")

#Checks if specified user is Revehound, then if specified user is aTPB, then if specified user is bot, else picks percentage for specified user
    if member == member:

        if member.id == (725050369339687045):
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"{member.mention} is 69% stupid!")

        elif member.id == (931613722567385138):
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"{member.mention} is 100% stupid!")

        elif member == bot.user:
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"I'm too smart, aborting calculation...")

        else:
            message = await ctx.channel.send("Calculating...")
            await asyncio.sleep(3)
            await message.edit(content=f"{member.mention} is {percentage}% stupid!")


#SAY COMMAND
@bot.command(help="Says what you say")
async def say(ctx, *, message=None):
    if message == None:
        await ctx.channel.send('You need to say something so I can say it back...')
    else:
        await ctx.channel.send(message)


keep_alive()

TOKEN = os.environ.get("DISCORD_TOKEN")

bot.run(TOKEN)