import discord
import time

from discord import app_commands
from discord.ext import commands

from discord.app_commands import AppCommandError, Choice


class General(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    
    #PING COMMAND
    @app_commands.command(name="ping", description="Shows the latency of the bot!")
    @app_commands.checks.cooldown(1, 10.0)
    async def ping(self, interaction: discord.Interaction):
        embed = discord.Embed(
                title="Ping/Latency",
                description='Ping: {0}ms'.format(round(self.bot.latency, 3)),
                color=0xb40000
            )
        await interaction.response.send_message(embed=embed)


    @ping.error
    async def ping_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


    @app_commands.command(name="serverinfo", description="Get information about this server!",)
    @app_commands.checks.cooldown(1, 10.0)
    async def serverinfo(self, interaction: discord.Interaction) -> None:
        guild = interaction.guild
        if guild is None:
            raise RuntimeError() #Exactly what `assert guild is not None` does
        icon = guild.icon
        if icon is None:
            raise RuntimeError()
        embed = discord.Embed(title=f"{interaction.guild}", description=" ", color=0xb40000)
        embed.set_thumbnail(
            url=icon.url
            )
        embed.add_field(
            name="Member Count",
            value=guild.member_count
            )
        embed.add_field(
            name="Role Count",
            value=len(guild.roles)
            )
        embed.add_field(
            name="Channels",
            value=f"{len(guild.channels)}"
            )
        embed.add_field(
            name="Booster Status",
            value=guild.premium_subscription_count
            )
        embed.add_field(
            name="Created at",
            value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S")
            )
        if guild.owner_id == 640145015800332328:
            embed.add_field(
                name="Owner",
                value="The one and only TimelessOn15Hz (thank you, thank you)",
                inline=False
                )
        else:
            embed.add_field(
                name="Owner",
                value=guild.owner,
                inline=False
                )
        await interaction.response.send_message(embed=embed)


    @serverinfo.error
    async def serverinfo_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


    #WHOMADETHIS COMMAND
    @app_commands.command(name="whomadethis", description="Who made this bot?",)
    @app_commands.checks.cooldown(1, 10.0)
    async def whomadethis(self, interaction: discord.Interaction) -> None:
        user = await self.bot.fetch_user(640145015800332328)
        pfp = user.avatar
        embed = discord.Embed(title="TeeTwoNot made this!", description="Check out my socials!", color=0xb40000)
        embed.set_thumbnail(url=pfp)

        embed.add_field(
            name="YouTube", 
            value="[Timeless](https://www.youtube.com/@teetwonot)" #Alternative: https://www.youtube.com/channel/UC_E94MhLA5QDCefWXLqW33A
            )
        embed.add_field(
            name="TikTok", 
            value="[TeeTwoNot](https://tiktok.com/@teetwonot)"
            )
        embed.add_field(
            name="Instagram", 
            value="[TeeTwoNot](https://instagram.com/teetwonot)"
            )
        embed.add_field(
            name="Twitch", 
            value="[TeeTwoNot](https://twitch.tv/teetwonot)"
            )
        embed.add_field(
            name="Website/Portfolio", 
            value="[TeeTwoNot](https://teetwonot.com)"
            )
        embed.add_field(
            name="Discord Server", 
            value="[Timeless28](https://discord.gg/ZmjXmfvxHU)"
            )
        await interaction.response.send_message(embed=embed)


    @whomadethis.error
    async def socials_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)


    #BAM COMMAND
    @app_commands.command(name="bam", description="Bams a user!")
    @app_commands.checks.cooldown(1, 5.0)
    async def bam(self, interaction: discord.Interaction):
        await interaction.response.send_message('https://imgur.com/a/e3g5W37')


    @bam.error
    async def bam_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

    #FLAG COMMAND
    @app_commands.command(name="flag", description="Shows the flag of Flevaria")
    @app_commands.checks.cooldown(1, 5.0)
    async def flag(self, interaction: discord.Interaction):
        await interaction.response.send_message('https://cdn.discordapp.com/attachments/807692974816886878/1149027815740686427/Flevarian_Flag.png')


    @flag.error
    async def flag_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

    #MAP COMMAND
    @app_commands.command(name="map", description="Shows the map of Flevaria")
    @app_commands.checks.cooldown(1, 5.0)
    async def map(self, interaction: discord.Interaction):
        await interaction.response.send_message('https://cdn.discordapp.com/attachments/1010331746920824944/1141045878866595860/Map_of_Flevaria.jpg')


    @map.error
    async def map_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

    #EXCHANGE COMMAND
    @app_commands.command(name="exchange", description="Shows the exchange rates of the Flevarian Obol")
    @app_commands.checks.cooldown(1, 5.0)
    @app_commands.choices(currency = [
        Choice(name = 'EUR -> FOB', value = "eur_fob"),
        Choice(name = 'FOB -> EUR', value = "fob_eur")
        ]
    )
    async def exchange(self, interaction: discord.Interaction, currency: str, amount: float):
        if currency == "eur_fob":
            converted = amount * 20
            embed = discord.Embed(
                title="Exchange Rate (EUR -> FOB)",
                description='',
                color=0xb40000
                )
            if converted == 1:
                embed.add_field(name="", value=f"{amount} Euro = {converted} Flevarian Obol")
            else:
                embed.add_field(name="", value=f"{amount} Euro = {converted} Flevarian Obols")
        elif currency == "fob_eur":
            converted = amount / 20
            embed = discord.Embed(
                title="Exchange Rate (FOB -> EUR)",
                description='',
                color=0xb40000
                )
            if amount == 1:
                embed.add_field(name="", value=f"{amount} Flevarian Obol = {converted} Euro")
            else:
                embed.add_field(name="", value=f"{amount} Flevarian Obols = {converted} Euro")
        await interaction.response.send_message(embed=embed)


    @exchange.error
    async def exchange_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

    #MOTTO COMMAND
    @app_commands.command(name="motto", description="All hail Babis!")
    @app_commands.checks.cooldown(1, 5.0)
    async def motto(self, interaction: discord.Interaction):
        await interaction.response.send_message('All hail Babis! <:babis:1013400927421599845>')


    @motto.error
    async def motto_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

    #DEMCHECK COMMAND
    @app_commands.command(name="demcheck", description="All hail Babis!")
    @app_commands.checks.cooldown(1, 5.0)
    async def demcheck(self, interaction: discord.Interaction):
        await interaction.response.send_message('"Our democracy is the most bestest in da whole world."\n> Democracy Inspector')
        await interaction.followup.send('https://cdn.discordapp.com/attachments/871684957133738014/1137862354848202813/VideoCapture_20221106-145808.jpg')


    @demcheck.error
    async def demcheck_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

    #SAY COMMAND
    @app_commands.command(name="say", description="All hail Babis!")
    @app_commands.checks.cooldown(1, 5.0)
    async def say(self, interaction: discord.Interaction, what: str = None):
        if what == None:
            await interaction.response.send_message("You gotta say something so I can say it back dude")
        else:
            await interaction.response.send_message(what)


    @say.error
    async def say_error(self, interaction: discord.Interaction, error: AppCommandError) -> None:
        if isinstance(error, app_commands.CommandOnCooldown):
            unixtime = int(time.time())
            totaltime = unixtime + int(error.retry_after)
            embed = discord.Embed(
                title="Slow down!",
                description=f"You can use this command again <t:{totaltime}:R>",
                color=0xb40000
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
    

async def setup(bot):
    await bot.add_cog(General(bot))