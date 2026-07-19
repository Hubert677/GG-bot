import discord
from discord.ext import commands
from config import DISCORD_TOKEN
import os
import asyncio
from datetime import datetime
from flask import Flask
from threading import Thread

# Flask app dla Render health check
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bot is running!', 200

def run_flask():
    """Uruchom Flask na porcie 5000 (wymagane przez Render)"""
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

# Intents - bez privileged intents
intents = discord.Intents.default()

# Bot (bez prefiksu - tylko slash komendy)
bot = commands.Bot(command_prefix="!", intents=intents)
bot.start_time = datetime.now()

@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    
    # Synchronizuj slash komendy
    try:
        synced = await bot.tree.sync()
        print(f"✅ Zsynchronizowano {len(synced)} slash komend")
    except Exception as e:
        print(f"❌ Błąd przy synchronizacji: {e}")

# Załaduj cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"Załadowano cog: {filename}")

async def main():
    async with bot:
        await load_cogs()
        # Tylko loguj jeśli token nie jest placeholder
        if DISCORD_TOKEN != "placeholder":
            await bot.start(DISCORD_TOKEN)
        else:
            print("❌ BŁĄD: Token jest placeholder - sprawdź ustawienia na Render!")
            print("⏳ Flask server jest uruchomiony na porcie 5000")
            # Czekaj nieskończenie aby Flask mógł działać
            await asyncio.sleep(86400)

if __name__ == "__main__":
    # Uruchom Flask w osobnym threadu
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print("Flask server uruchomiony na porcie 5000")
    
    # Uruchom Discord bota
    asyncio.run(main())

