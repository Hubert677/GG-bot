import discord
from discord.ext import commands
from discord import app_commands
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

    def is_admin(self, interaction: discord.Interaction):
        return interaction.user.guild_permissions.administrator

    @app_commands.command(name='create-ticket', description='Stwórz nowy ticket')
    async def create_ticket(self, interaction: discord.Interaction, reason: str = "Brak opisu"):
        """Stwórz nowy ticket"""
        guild = interaction.guild
        
        # Sprawdź czy już ma otwarty ticket
        tickets = [ch for ch in guild.text_channels if ch.name.startswith(f"ticket-{interaction.user.id}")]
        if tickets:
            await interaction.response.send_message(f"❌ Masz już otwarty ticket! {tickets[0].mention}", ephemeral=True)
            return

        # Stwórz channel
        try:
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{interaction.user.id}",
                topic=f"Ticket od {interaction.user} - {reason}"
            )
            
            # Ustaw permisje
            await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
            
            embed = discord.Embed(
                title="🎫 Nowy Ticket",
                description=f"**Użytkownik:** {interaction.user.mention}\n**Powód:** {reason}",
                color=discord.Color.green()
            )
            await ticket_channel.send(embed=embed)
            await interaction.response.send_message(f"✅ Ticket stworzony! {ticket_channel.mention}")
        except Exception as e:
            await interaction.response.send_message(f"❌ Błąd przy tworzeniu ticketa: {e}", ephemeral=True)

    @app_commands.command(name='close-ticket', description='Zamknij ticket (ADMIN)')
    async def close_ticket(self, interaction: discord.Interaction):
        """Zamknij ticket (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return

        if not interaction.channel.name.startswith("ticket-"):
            await interaction.response.send_message("❌ To nie jest channel ticketa!", ephemeral=True)
            return

        embed = discord.Embed(
            title="🎫 Ticket Zamknięty",
            description=f"Ticket zamknięty przez {interaction.user.mention}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed)
        await interaction.channel.delete(reason="Ticket zamknięty")

async def setup(bot):
    await bot.add_cog(Tickets(bot))

