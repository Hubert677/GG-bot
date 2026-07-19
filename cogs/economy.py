import discord
from discord.ext import commands
from discord import app_commands
import json
import os
import random
from datetime import datetime, timedelta

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "economy_config.json"
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

    def get_user_data(self, user_id: str):
        if user_id not in self.config:
            self.config[user_id] = {
                "balance": 0,
                "inventory": {},
                "last_work": 0,
                "last_daily": 0
            }
        return self.config[user_id]

    # SHOP ITEMS
    SHOP_ITEMS = {
        "apple": {"price": 10, "emoji": "🍎", "name": "Jabłko"},
        "burger": {"price": 25, "emoji": "🍔", "name": "Burger"},
        "pizza": {"price": 50, "emoji": "🍕", "name": "Pizza"},
        "sushi": {"price": 75, "emoji": "🍣", "name": "Sushi"},
        "diamond": {"price": 200, "emoji": "💎", "name": "Diament"},
        "gold": {"price": 150, "emoji": "🏆", "name": "Złoto"},
    }

    @app_commands.command(name="balance", description="Sprawdź swój portfel")
    async def balance(self, interaction: discord.Interaction, user: discord.User = None):
        """Sprawdź saldo"""
        user = user or interaction.user
        user_id = str(user.id)
        data = self.get_user_data(user_id)
        
        embed = discord.Embed(
            title=f"💰 Portfel {user.name}",
            color=discord.Color.gold()
        )
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="💵 Saldo", value=f"**{data['balance']} 💵**", inline=False)
        embed.add_field(name="📦 Przedmioty", value=f"Razem: {len(data['inventory'])} item", inline=False)
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="work", description="Pracuj i zarabiaj pieniądze")
    async def work(self, interaction: discord.Interaction):
        """Pracuj"""
        user_id = str(interaction.user.id)
        data = self.get_user_data(user_id)
        
        # Cooldown 30 minut
        last_work = data.get("last_work", 0)
        if datetime.now().timestamp() - last_work < 1800:
            remaining = int(1800 - (datetime.now().timestamp() - last_work))
            minutes = remaining // 60
            await interaction.response.send_message(
                f"❌ Musisz czekać {minutes}m przed następną pracą!",
                ephemeral=True
            )
            return
        
        # Losowa wypłata 15-50
        earnings = random.randint(15, 50)
        data["balance"] += earnings
        data["last_work"] = datetime.now().timestamp()
        self.save_config()
        
        embed = discord.Embed(
            title="💼 Praca Skończona",
            description=f"Zarobiłeś **{earnings} 💵**\n\nNoue saldo: **{data['balance']} 💵**",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="daily", description="Odbierz bonus codzienny")
    async def daily(self, interaction: discord.Interaction):
        """Bonus dzienny"""
        user_id = str(interaction.user.id)
        data = self.get_user_data(user_id)
        
        # Cooldown 24 godziny
        last_daily = data.get("last_daily", 0)
        if datetime.now().timestamp() - last_daily < 86400:
            remaining = int(86400 - (datetime.now().timestamp() - last_daily))
            hours = remaining // 3600
            await interaction.response.send_message(
                f"❌ Musisz czekać {hours}h na następny bonus!",
                ephemeral=True
            )
            return
        
        bonus = 100
        data["balance"] += bonus
        data["last_daily"] = datetime.now().timestamp()
        self.save_config()
        
        embed = discord.Embed(
            title="🎁 Bonus Codzienny",
            description=f"Otrzymałeś **{bonus} 💵**\n\nNoue saldo: **{data['balance']} 💵**",
            color=discord.Color.purple()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="shop", description="Pokaż sklep z przedmiotami")
    async def shop(self, interaction: discord.Interaction):
        """Pokaż sklep"""
        shop_str = ""
        for item_id, item_data in self.SHOP_ITEMS.items():
            shop_str += f"{item_data['emoji']} **{item_data['name']}** - {item_data['price']} 💵\n"
        
        embed = discord.Embed(
            title="🛒 Sklep",
            description=shop_str + "\nUżyj `/buy [item]` aby kupić",
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="buy", description="Kup przedmiot ze sklepu")
    async def buy(self, interaction: discord.Interaction, item: str):
        """Kup przedmiot"""
        if item not in self.SHOP_ITEMS:
            await interaction.response.send_message("❌ Taki przedmiot nie istnieje!", ephemeral=True)
            return
        
        user_id = str(interaction.user.id)
        data = self.get_user_data(user_id)
        
        item_data = self.SHOP_ITEMS[item]
        price = item_data["price"]
        
        if data["balance"] < price:
            await interaction.response.send_message(
                f"❌ Brak pieniędzy! Potrzebujesz {price} 💵, masz {data['balance']} 💵",
                ephemeral=True
            )
            return
        
        data["balance"] -= price
        if item not in data["inventory"]:
            data["inventory"][item] = 0
        data["inventory"][item] += 1
        self.save_config()
        
        embed = discord.Embed(
            title="✅ Zakup Pomyślny",
            description=f"Kupiłeś **{item_data['name']}** {item_data['emoji']}\n\nKoszt: {price} 💵\nNoue saldo: **{data['balance']} 💵**",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="inventory", description="Pokaż swoje przedmioty")
    async def inventory(self, interaction: discord.Interaction):
        """Pokaż inventory"""
        user_id = str(interaction.user.id)
        data = self.get_user_data(user_id)
        
        if not data["inventory"]:
            await interaction.response.send_message("📦 Twój plecak jest pusty!", ephemeral=True)
            return
        
        inventory_str = ""
        for item_id, count in data["inventory"].items():
            item_data = self.SHOP_ITEMS[item_id]
            inventory_str += f"{item_data['emoji']} **{item_data['name']}** x{count}\n"
        
        embed = discord.Embed(
            title="📦 Mój Plecak",
            description=inventory_str,
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="gamble", description="Graj w grę o pieniądze!")
    async def gamble(self, interaction: discord.Interaction, bet: int):
        """Gra - RPS"""
        user_id = str(interaction.user.id)
        data = self.get_user_data(user_id)
        
        if data["balance"] < bet:
            await interaction.response.send_message(
                f"❌ Niewystarczające środki! Masz {data['balance']} 💵",
                ephemeral=True
            )
            return
        
        choices = ["Papier", "Kamień", "Nożyce"]
        bot_choice = random.choice(choices)
        your_choice = random.choice(choices)
        
        # Logika gry
        if your_choice == bot_choice:
            result = "🤝 Remis!"
            outcome = 0
        elif (your_choice == "Papier" and bot_choice == "Kamień") or \
             (your_choice == "Kamień" and bot_choice == "Nożyce") or \
             (your_choice == "Nożyce" and bot_choice == "Papier"):
            result = f"🎉 Wygrałeś {bet*2} 💵!"
            outcome = bet * 2
        else:
            result = f"😢 Przegrałeś {bet} 💵!"
            outcome = -bet
        
        data["balance"] += outcome
        self.save_config()
        
        embed = discord.Embed(
            title="🎰 Gra - Papier Kamień Nożyce",
            description=f"Twój wybór: **{your_choice}**\nMój wybór: **{bot_choice}**\n\n{result}\n\nNoue saldo: **{data['balance']} 💵**",
            color=discord.Color.orange()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="transfer", description="Prześlij pieniądze innej osobie")
    async def transfer(self, interaction: discord.Interaction, user: discord.User, amount: int):
        """Prześlij pieniądze"""
        if amount <= 0:
            await interaction.response.send_message("❌ Kwota musi być większa niż 0!", ephemeral=True)
            return
        
        sender_id = str(interaction.user.id)
        receiver_id = str(user.id)
        
        sender_data = self.get_user_data(sender_id)
        receiver_data = self.get_user_data(receiver_id)
        
        if sender_data["balance"] < amount:
            await interaction.response.send_message(
                f"❌ Niewystarczające środki! Masz {sender_data['balance']} 💵",
                ephemeral=True
            )
            return
        
        sender_data["balance"] -= amount
        receiver_data["balance"] += amount
        self.save_config()
        
        embed = discord.Embed(
            title="💸 Transfer Pomyślny",
            description=f"Przesłałeś **{amount} 💵** do {user.mention}\n\nTwoje nowe saldo: **{sender_data['balance']} 💵**",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Economy(bot))
