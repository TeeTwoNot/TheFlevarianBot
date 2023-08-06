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
        embed = discord.Embed(title="TimelessOn15Hz made this!", description="Check out my socials!", color=0xb40000)
        embed.set_thumbnail(url=pfp)

        embed.add_field(
            name="YouTube", 
            value="[Timeless](https://www.youtube.com/@timelesson15hz)" #Alternative: https://www.youtube.com/channel/UC_E94MhLA5QDCefWXLqW33A
            )
        embed.add_field(
            name="TikTok", 
            value="[TimelessOn15Hz](https://tiktok.com/@timelesson15hz)"
            )
        embed.add_field(
            name="Instagram", 
            value="[TimelessOn15Hz](https://instagram.com/timelesson15hz)"
            )
        embed.add_field(
            name="Twitch", 
            value="[TimelessOn15Hz](https://twitch.tv/timelesson15hz)"
            )
        embed.add_field(
            name="Website/Portfolio", 
            value="[ChrTsk](https://chrtsk.com)"
            )
        embed.add_field(
            name="Discord Server", 
            value="[Timeless28](https://discord.gg/DsE6CFB6VK)"
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
        await interaction.response.send_message('https://cdn.discordapp.com/attachments/1010331746920824944/1137176962671054920/Flag_of_Bambenia.png')


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
        await interaction.response.send_message('https://cdn.discordapp.com/attachments/1010331746920824944/1137177381635895447/2023-07-13-18-28-53-660.jpg')


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
    @app_commands.command(name="exchange", description="Shows the exchange rates of FOB")
    @app_commands.checks.cooldown(1, 5.0)
    @app_commands.choices(currency = [
        Choice(name = 'EUR -> FOB', value = "eur_fob"),
        Choice(name = 'FOB -> EUR', value = "fob_eur")
        ]
    )
    async def exchange(self, interaction: discord.Interaction, currency: str, amount: int):
        if currency == "eur_fob":
            converted = amount * 20
            embed = discord.Embed(
                title="Exchange Rate (EUR -> FOB)",
                description='',
                color=0xb40000
                )
            embed.add_field(name=f"{amount} = {converted}")
            await interaction.response.send_message(embed=embed)
        
        elif currency == "fob_eur":
            converted = amount / 20
            embed = discord.Embed(
                title="Exchange Rate (FOB -> EUR)",
                description='',
                color=0xb40000
                )
            embed.add_field(name=f"{amount} = {converted}")
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
    

async def setup(bot):
    await bot.add_cog(General(bot))