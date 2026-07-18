import discord
from discord.ext import commands
from discord import app_commands
import json
import os
from datetime import datetime

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
    @app_commands.choices(ticket_type=[
        app_commands.Choice(name="🐛 Bug Report", value="bug"),
        app_commands.Choice(name="✨ Feature Request", value="feature"),
        app_commands.Choice(name="🆘 Support/Pomoc", value="support"),
    ])
    async def create_ticket(self, interaction: discord.Interaction, ticket_type: app_commands.Choice[str], reason: str):
        """Stwórz nowy ticket z typem"""
        guild = interaction.guild
        
        # Sprawdź czy już ma otwarty ticket
        tickets = [ch for ch in guild.text_channels if ch.name.startswith(f"ticket-{interaction.user.id}")]
        if tickets:
            await interaction.response.send_message(f"❌ Masz już otwarty ticket! {tickets[0].mention}", ephemeral=True)
            return

        # Mapuj type na emoji i pełną nazwę
        type_map = {
            "bug": ("🐛", "Bug Report"),
            "feature": ("✨", "Feature Request"),
            "support": ("🆘", "Support/Pomoc")
        }
        emoji, type_name = type_map[ticket_type.value]

        # Stwórz channel
        try:
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{interaction.user.id}",
                topic=f"{emoji} Ticket: {type_name} - {reason}",
                category=None
            )
            
            # Ustaw permisje
            await ticket_channel.set_permissions(interaction.user, read_messages=True, send_messages=True)
            
            embed = discord.Embed(
                title=f"{emoji} Nowy Ticket",
                description=f"**Użytkownik:** {interaction.user.mention}\n**Typ:** {type_name}\n**Powód:** {reason}",
                color=discord.Color.green()
            )
            
            # Dodaj przycisk do zamknięcia
            embed.add_field(name="ℹ️ Info", value="Użyj `/close-ticket` aby zamknąć ten ticket", inline=False)
            embed.add_field(name="📅 Stworzony", value=f"<t:{int(datetime.now().timestamp())}:F>", inline=False)
            
            await ticket_channel.send(embed=embed)
            await interaction.response.send_message(f"✅ Ticket **{type_name}** stworzony! {ticket_channel.mention}")
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

