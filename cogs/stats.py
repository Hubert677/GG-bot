import discord
from discord.ext import commands
from discord import app_commands
import json
import os
from datetime import datetime

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "stats_config.json"
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        else:
            self.config = {}

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def add_xp(self, user_id: str, amount: int = 1):
        """Dodaj XP użytkownikowi"""
        if user_id not in self.config:
            self.config[user_id] = {"xp": 0, "level": 0}
        
        self.config[user_id]["xp"] += amount
        self.config[user_id]["level"] = self.config[user_id]["xp"] // 100
        self.save_config()

    @app_commands.command(name="profile", description="Pokaż profil użytkownika")
    async def profile(self, interaction: discord.Interaction, user: discord.User = None):
        """Pokaż profil"""
        user = user or interaction.user
        user_id = str(user.id)
        
        if user_id not in self.config:
            self.config[user_id] = {"xp": 0, "level": 0}
            self.save_config()
        
        stats = self.config[user_id]
        
        embed = discord.Embed(
            title=f"📊 Profil {user.name}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="🎖️ Poziom", value=stats["level"], inline=True)
        embed.add_field(name="⭐ XP", value=stats["xp"], inline=True)
        embed.add_field(name="📈 XP do następnego poziomu", value=f"{stats['xp'] % 100}/100", inline=True)
        embed.add_field(name="📅 Konto stworzone", value=f"<t:{int(user.created_at.timestamp())}:D>", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="leaderboard", description="Pokaż ranking użytkowników")
    async def leaderboard(self, interaction: discord.Interaction):
        """Pokaż leaderboard"""
        if not self.config:
            await interaction.response.send_message("❌ Brak danych!", ephemeral=True)
            return
        
        # Sortuj po XP
        sorted_users = sorted(self.config.items(), key=lambda x: x[1]["xp"], reverse=True)[:10]
        
        leaderboard_str = ""
        for i, (user_id, stats) in enumerate(sorted_users, 1):
            try:
                user = await self.bot.fetch_user(int(user_id))
                leaderboard_str += f"{i}. **{user.name}** - Lvl {stats['level']} ({stats['xp']} XP)\n"
            except:
                leaderboard_str += f"{i}. Nieznany użytkownik - Lvl {stats['level']} ({stats['xp']} XP)\n"
        
        embed = discord.Embed(
            title="🏆 Ranking Użytkowników",
            description=leaderboard_str,
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="addxp", description="Dodaj XP użytkownikowi (ADMIN)")
    async def addxp(self, interaction: discord.Interaction, user: discord.User, amount: int):
        """Dodaj XP użytkownikowi"""
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("❌ Brak uprawnień!", ephemeral=True)
            return
        
        for _ in range(amount):
            self.add_xp(str(user.id), 1)
        
        user_id = str(user.id)
        stats = self.config[user_id]
        
        embed = discord.Embed(
            title="✅ XP Dodane",
            description=f"**Użytkownik:** {user.mention}\n**Dodano:** {amount} XP\n**Razem XP:** {stats['xp']}\n**Poziom:** {stats['level']}",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="topstats", description="Top 5 aktywnych użytkowników")
    async def topstats(self, interaction: discord.Interaction):
        """Top 5 statystyk"""
        if not self.config:
            await interaction.response.send_message("❌ Brak danych!", ephemeral=True)
            return
        
        sorted_users = sorted(self.config.items(), key=lambda x: x[1]["xp"], reverse=True)[:5]
        
        stats_str = ""
        for i, (user_id, stats) in enumerate(sorted_users, 1):
            try:
                user = await self.bot.fetch_user(int(user_id))
                stats_str += f"{i}. {user.mention} - **{stats['xp']}** XP\n"
            except:
                stats_str += f"{i}. Nieznany użytkownik - **{stats['xp']}** XP\n"
        
        embed = discord.Embed(
            title="🔝 Top 5 Aktywnych",
            description=stats_str,
            color=discord.Color.purple()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Stats(bot))
