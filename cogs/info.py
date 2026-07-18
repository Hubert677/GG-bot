import discord
from discord.ext import commands
from datetime import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        """Pokaż listę komend"""
        embed = discord.Embed(
            title="📚 Komendy Bota",
            description="Poniżej znajduje się lista wszystkich dostępnych komend",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📌 Ogólne",
            value="`!ping` - Sprawdź latencję\n`!help` - Lista komend\n`!info` - Info o bocie",
            inline=False
        )
        
        embed.add_field(
            name="🎫 Tickety",
            value="`!create-ticket [powód]` - Stwórz ticket\n`!close-ticket` - Zamknij ticket (ADMIN)",
            inline=False
        )
        
        embed.add_field(
            name="👋 Powitania/Pożegnania",
            value="`!set-welcome [wiadomość]` - Ustaw powitanie (ADMIN)\n`!set-goodbye [wiadomość]` - Ustaw pożegnanie (ADMIN)",
            inline=False
        )
        
        embed.add_field(
            name="🔨 Moderacja",
            value="`!ban @user [powód]` - Zbanuj (ADMIN)\n`!kick @user [powód]` - Wyrzuć (ADMIN)\n`!warn @user [powód]` - Ostrzeż (ADMIN)\n`!clear [ilość]` - Usuń wiadomości (ADMIN)",
            inline=False
        )
        
        embed.set_footer(text="Wpisz !info aby dowiedzieć się więcej o bocie")
        await ctx.send(embed=embed)

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Sprawdź latencję bota"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latencja: `{latency}ms`",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command(name='info')
    async def info(self, ctx):
        """Informacje o bocie"""
        embed = discord.Embed(
            title="🤖 GG-Bot",
            description="Discord bot stworzony w Python z discord.py",
            color=discord.Color.purple()
        )
        
        embed.add_field(name="👨‍💻 Autor", value="Hubert677", inline=False)
        embed.add_field(name="📦 Wersja", value="1.0", inline=False)
        embed.add_field(name="🔗 GitHub", value="[GG-bot](https://github.com/Hubert677/GG-bot)", inline=False)
        embed.add_field(name="⚙️ Prefix", value="`!`", inline=False)
        embed.add_field(name="📅 Data uruchomienia", value=f"<t:{int(datetime.now().timestamp())}:F>", inline=False)
        
        embed.set_footer(text="Wpisz !help aby zobaczyć wszystkie komendy")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
