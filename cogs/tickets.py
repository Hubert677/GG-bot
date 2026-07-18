import discord
from discord.ext import commands
import json
import os

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "tickets_config.json"
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

    def is_admin(self, ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command(name='create-ticket')
    async def create_ticket(self, ctx, *, reason="Brak opisu"):
        """Stwórz nowy ticket"""
        guild = ctx.guild
        
        # Sprawdź czy już ma otwarty ticket
        tickets = [ch for ch in guild.text_channels if ch.name.startswith(f"ticket-{ctx.author.id}")]
        if tickets:
            await ctx.send(f"❌ Masz już otwarty ticket! {tickets[0].mention}")
            return

        # Stwórz channel
        try:
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{ctx.author.id}",
                topic=f"Ticket od {ctx.author} - {reason}"
            )
            
            # Ustaw permisje
            await ticket_channel.set_permissions(ctx.author, read_messages=True, send_messages=True)
            
            embed = discord.Embed(
                title="🎫 Nowy Ticket",
                description=f"**Użytkownik:** {ctx.author.mention}\n**Powód:** {reason}",
                color=discord.Color.green()
            )
            await ticket_channel.send(embed=embed)
            await ctx.send(f"✅ Ticket stworzony! {ticket_channel.mention}")
        except Exception as e:
            await ctx.send(f"❌ Błąd przy tworzeniu ticketa: {e}")

    @commands.command(name='close-ticket')
    async def close_ticket(self, ctx):
        """Zamknij ticket (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return

        if not ctx.channel.name.startswith("ticket-"):
            await ctx.send("❌ To nie jest channel ticketa!")
            return

        embed = discord.Embed(
            title="🎫 Ticket Zamknięty",
            description=f"Ticket zamknięty przez {ctx.author.mention}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        await ctx.channel.delete(reason="Ticket zamknięty")

async def setup(bot):
    await bot.add_cog(Tickets(bot))
