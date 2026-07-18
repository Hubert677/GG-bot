import discord
from discord.ext import commands
from config import DISCORD_TOKEN, PREFIX

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")
    print(f"Bot ID: {bot.user.id}")

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
    import asyncio
    import os
    asyncio.run(main())
