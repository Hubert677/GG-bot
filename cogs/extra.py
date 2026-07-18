import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="botinfo", description="Informacje o bocie")
    async def botinfo(self, interaction: discord.Interaction):
        """Szczegółowe info o bocie"""
        embed = discord.Embed(
            title="🤖 Informacje o Bocie",
            description="GG-Bot - Wszechstronny Discord Bot",
            color=discord.Color.blue()
        )
        
        embed.add_field(name="👨‍💻 Autor", value="Hubert677", inline=False)
        embed.add_field(name="📦 Wersja", value="3.0", inline=False)
        embed.add_field(name="🔗 GitHub", value="[GG-Bot](https://github.com/Hubert677/GG-bot)", inline=False)
        embed.add_field(name="💻 Język", value="Python 3.8+ (discord.py)", inline=False)
        embed.add_field(name="⚡ Prefix", value="Slash komendy (`/`)", inline=False)
        embed.add_field(name="🎮 Funkcje", value="17+ komend (zabawa, moderacja, role, statystyki)", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="guildinfo", description="Szczegółowe info o serwerze")
    async def guildinfo(self, interaction: discord.Interaction):
        """Info o serwerze"""
        guild = interaction.guild
        
        embed = discord.Embed(
            title=f"🏰 {guild.name}",
            description=f"ID: {guild.id}",
            color=discord.Color.purple()
        )
        
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(name="👥 Członkowie", value=guild.member_count, inline=True)
        embed.add_field(name="👑 Właściciel", value=guild.owner.mention, inline=True)
        embed.add_field(name="🌍 Region", value=str(guild.region) if guild.region else "N/A", inline=True)
        embed.add_field(name="📅 Stworzony", value=f"<t:{int(guild.created_at.timestamp())}:F>", inline=False)
        embed.add_field(name="💬 Kanały tekstowe", value=len(guild.text_channels), inline=True)
        embed.add_field(name="🔊 Kanały głosowe", value=len(guild.voice_channels), inline=True)
        embed.add_field(name="🏷️ Role", value=len(guild.roles), inline=True)
        embed.add_field(name="📊 Poziom weryfikacji", value=str(guild.verification_level), inline=True)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="uptime", description="Jak długo bot działa")
    async def uptime(self, interaction: discord.Interaction):
        """Uptime bota"""
        uptime_seconds = (datetime.now() - self.bot.start_time).total_seconds() if hasattr(self.bot, 'start_time') else 0
        
        days = int(uptime_seconds // 86400)
        hours = int((uptime_seconds % 86400) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        
        embed = discord.Embed(
            title="⏱️ Uptime Bota",
            description=f"{days}d {hours}h {minutes}m",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="members", description="Info o członkach serwera")
    async def members(self, interaction: discord.Interaction):
        """Info o członkach"""
        guild = interaction.guild
        total_members = guild.member_count
        online_members = sum(1 for m in guild.members if m.status != discord.Status.offline)
        bots = sum(1 for m in guild.members if m.bot)
        humans = total_members - bots
        
        embed = discord.Embed(
            title="👥 Członkowie Serwera",
            color=discord.Color.blue()
        )
        
        embed.add_field(name="🟢 Online", value=online_members, inline=True)
        embed.add_field(name="⚫ Offline", value=total_members - online_members, inline=True)
        embed.add_field(name="👤 Ludzie", value=humans, inline=True)
        embed.add_field(name="🤖 Boty", value=bots, inline=True)
        embed.add_field(name="📊 Razem", value=total_members, inline=True)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="slowmode", description="Ustaw tryb powolny kanału (ADMIN)")
    async def slowmode(self, interaction: discord.Interaction, seconds: int):
        """Ustaw slowmode kanału"""
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ Brak uprawnień!", ephemeral=True)
            return
        
        if seconds < 0 or seconds > 21600:
            await interaction.response.send_message("❌ Czas musi być między 0 a 21600 sekund!", ephemeral=True)
            return
        
        await interaction.channel.edit(slowmode_delay=seconds)
        
        if seconds == 0:
            await interaction.response.send_message("✅ Tryb powolny wyłączony!")
        else:
            await interaction.response.send_message(f"✅ Tryb powolny ustawiony na {seconds}s!")

async def setup(bot):
    await bot.add_cog(Extra(bot))
