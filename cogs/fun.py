import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="8ball", description="Magiczna kula 8 - zadaj pytanie!")
    async def eight_ball(self, interaction: discord.Interaction, question: str):
        """Magiczna kula 8"""
        responses = [
            "Zdecydowanie tak! ✅",
            "Tak, bez wątpienia 👍",
            "Wygląda na to, że tak 😊",
            "Zapytaj później 🤔",
            "Nie mogę teraz orzec 🤷",
            "Nie 🚫",
            "Zdecydowanie nie! ❌",
            "Bardzo wątpliwe 😐",
            "Szanse są małe 📉",
            "Wszystko wskazuje na tak 🎯",
        ]
        
        embed = discord.Embed(
            title="🔮 Magiczna Kula 8",
            description=f"**Pytanie:** {question}\n\n**Odpowiedź:** {random.choice(responses)}",
            color=discord.Color.purple()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="coin", description="Rzut monetą")
    async def coin(self, interaction: discord.Interaction):
        """Rzut monetą"""
        result = random.choice(["Orzeł 🦅", "Reszka 🪙"])
        embed = discord.Embed(
            title="🪙 Rzut Monetą",
            description=f"Wynik: **{result}**",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="dice", description="Rzut kostką d20")
    async def dice(self, interaction: discord.Interaction, sides: int = 20):
        """Rzut kostką"""
        if sides < 2 or sides > 1000:
            await interaction.response.send_message("❌ Kostka musi mieć 2-1000 ścian!", ephemeral=True)
            return
        
        result = random.randint(1, sides)
        embed = discord.Embed(
            title=f"🎲 Rzut Kostką d{sides}",
            description=f"Wynik: **{result}**",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="joke", description="Losowy kawał")
    async def joke(self, interaction: discord.Interaction):
        """Losowy kawał"""
        jokes = [
            "Dlaczego krowy noszą dzwonki? Bo tracą baseny! 🐄",
            "Jaki jest ulubiony napój bałwana? Lodowata kawa! ☃️",
            "Jak się mówi na kurę, która lata? Słowiańska siła! 🐔",
            "Ile nóg ma skarabeusz? 6, ale nie może biegać bo ma je w głowie! 🪲",
            "Czym się różni komputer od mózgu? Komputer ma mózg! 🧠",
        ]
        
        embed = discord.Embed(
            title="😂 Losowy Kawał",
            description=random.choice(jokes),
            color=discord.Color.yellow()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="rps", description="Papier, Kamień, Nożyce")
    async def rock_paper_scissors(self, interaction: discord.Interaction, choice: str):
        """Papier, Kamień, Nożyce"""
        valid_choices = ["papier", "kamień", "nożyce"]
        
        if choice.lower() not in valid_choices:
            await interaction.response.send_message(f"❌ Wybierz z: {', '.join(valid_choices)}", ephemeral=True)
            return
        
        bot_choice = random.choice(valid_choices)
        
        if choice.lower() == bot_choice:
            result = "🤝 Remis!"
        elif (choice.lower() == "kamień" and bot_choice == "nożyce") or \
             (choice.lower() == "papier" and bot_choice == "kamień") or \
             (choice.lower() == "nożyce" and bot_choice == "papier"):
            result = "🎉 Wygrałeś!"
        else:
            result = "😢 Przegrałeś!"
        
        embed = discord.Embed(
            title="🎮 Papier, Kamień, Nożyce",
            description=f"**Twój wybór:** {choice}\n**Mój wybór:** {bot_choice}\n\n{result}",
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
