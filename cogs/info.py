import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Pokaż listę wszystkich komend")
    async def help(self, interaction: discord.Interaction):
        """Pokaż listę komend"""
        embed = discord.Embed(
            title="📚 Komendy Bota",
            description="Poniżej znajduje się lista wszystkich dostępnych komend",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📌 Ogólne",
            value="`/ping` - Sprawdź latencję\n`/help` - Lista komend\n`/info` - Info o bocie\n`/user` - Info o użytkowniku\n`/server` - Info o serwerze\n`/avatar` - Avatar użytkownika\n`/stats` - Statystyki serwera",
            inline=False
        )
        
        embed.add_field(
            name="🎫 Tickety",
            value="`/create-ticket` - Stwórz ticket\n`/close-ticket` - Zamknij ticket (ADMIN)",
            inline=False
        )
        
        embed.add_field(
            name="👋 Powitania/Pożegnania",
            value="`/set-welcome` - Ustaw powitanie (ADMIN)\n`/set-goodbye` - Ustaw pożegnanie (ADMIN)",
            inline=False
        )
        
        embed.add_field(
            name="🔨 Moderacja",
            value="`/ban` - Zbanuj (ADMIN)\n`/kick` - Wyrzuć (ADMIN)\n`/warn` - Ostrzeż (ADMIN)\n`/clear` - Usuń wiadomości (ADMIN)",
            inline=False
        )
        
        embed.set_footer(text="Wpisz /info aby dowiedzieć się więcej o bocie")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="info", description="Informacje o bocie")
    async def info(self, interaction: discord.Interaction):
        """Informacje o bocie"""
        embed = discord.Embed(
            title="🤖 GG-Bot",
            description="Discord bot stworzony w Python z discord.py",
            color=discord.Color.purple()
        )
        
        embed.add_field(name="👨‍💻 Autor", value="Hubert677", inline=False)
        embed.add_field(name="📦 Wersja", value="2.0", inline=False)
        embed.add_field(name="🔗 GitHub", value="[GG-bot](https://github.com/Hubert677/GG-bot)", inline=False)
        embed.add_field(name="⚙️ Typ komend", value="Slash komendy (`/`)", inline=False)
        embed.add_field(name="📅 Data uruchomienia", value=f"<t:{int(datetime.now().timestamp())}:F>", inline=False)
        
        embed.set_footer(text="Wpisz /help aby zobaczyć wszystkie komendy")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))

