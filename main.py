import discord
from discord.ext import commands
from config import DISCORD_TOKEN, PREFIX
import os
import asyncio

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

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
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
