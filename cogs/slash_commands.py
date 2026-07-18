import discord
from discord.ext import commands
from discord import app_commands

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Sprawdź latencję bota")
    async def slash_ping(self, interaction: discord.Interaction):
        """Slash komenda ping"""
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"🏓 Pong! `{latency}ms`")

    @app_commands.command(name="user", description="Pokaż informacje o użytkowniku")
    async def slash_user(self, interaction: discord.Interaction, user: discord.User = None):
        """Slash komenda user info"""
        user = user or interaction.user
        
        embed = discord.Embed(
            title=f"👤 {user.name}",
            description=f"ID: {user.id}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="📅 Konto stworzone", value=f"<t:{int(user.created_at.timestamp())}:F>", inline=False)
        embed.add_field(name="🤖 Bot?", value="✅ Tak" if user.bot else "❌ Nie", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="server", description="Informacje o serwerze")
    async def slash_server(self, interaction: discord.Interaction):
        """Slash komenda server info"""
        guild = interaction.guild
        
        embed = discord.Embed(
            title=f"🏠 {guild.name}",
            description=f"ID: {guild.id}",
            color=discord.Color.purple()
        )
        embed.set_thumbnail(url=guild.icon)
        embed.add_field(name="👥 Członkowie", value=str(guild.member_count), inline=True)
        embed.add_field(name="📅 Stworzony", value=f"<t:{int(guild.created_at.timestamp())}:F>", inline=False)
        embed.add_field(name="👑 Właściciel", value=guild.owner.mention, inline=True)
        embed.add_field(name="📢 Kanały", value=f"💬 {len(guild.text_channels)} | 🔊 {len(guild.voice_channels)}", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="avatar", description="Pokaż avatar użytkownika")
    async def slash_avatar(self, interaction: discord.Interaction, user: discord.User = None):
        """Slash komenda avatar"""
        user = user or interaction.user
        
        embed = discord.Embed(
            title=f"Avatar dla {user.name}",
            color=discord.Color.green()
        )
        embed.set_image(url=user.avatar)
        embed.add_field(name="URL", value=f"[Kliknij tutaj]({user.avatar})", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="stats", description="Statystyki serwera")
    async def slash_stats(self, interaction: discord.Interaction):
        """Slash komenda server stats"""
        guild = interaction.guild
        
        # Liczenie roli
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        roles = len(guild.roles)
        members = guild.member_count
        bots = sum(1 for member in guild.members if member.bot)
        humans = members - bots
        
        embed = discord.Embed(
            title="📊 Statystyki Serwera",
            description=f"Statystyki dla {guild.name}",
            color=discord.Color.orange()
        )
        
        embed.add_field(name="👥 Członkowie", value=f"**Razem:** {members}\n**Ludzie:** {humans}\n**Boty:** {bots}", inline=True)
        embed.add_field(name="📢 Kanały", value=f"**Tekstowe:** {text_channels}\n**Głosowe:** {voice_channels}\n**Razem:** {text_channels + voice_channels}", inline=True)
        embed.add_field(name="🏷️ Role", value=str(roles), inline=True)
        embed.add_field(name="🌍 Region", value=str(guild.region) if guild.region else "Brak info", inline=True)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
