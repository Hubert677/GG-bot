import discord
from discord.ext import commands
from discord import app_commands
import json
import os

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "welcome_config.json"
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

    @app_commands.command(name='set-welcome', description='Ustaw wiadomość powitania dla nowych użytkowników (ADMIN)')
    async def set_welcome(self, interaction: discord.Interaction, message: str):
        """Ustaw wiadomość powitania dla nowych użytkowników (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return
        
        guild_id = str(interaction.guild.id)
        self.config[guild_id] = self.config.get(guild_id, {})
        self.config[guild_id]["welcome_message"] = message
        self.save_config()
        await interaction.response.send_message(f"✅ Wiadomość powitania ustawiona:\n`{message}`")

    @app_commands.command(name='set-goodbye', description='Ustaw wiadomość pożegnania dla użytkowników (ADMIN)')
    async def set_goodbye(self, interaction: discord.Interaction, message: str):
        """Ustaw wiadomość pożegnania dla użytkowników (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return
        
        guild_id = str(interaction.guild.id)
        self.config[guild_id] = self.config.get(guild_id, {})
        self.config[guild_id]["goodbye_message"] = message
        self.save_config()
        await interaction.response.send_message(f"✅ Wiadomość pożegnania ustawiona:\n`{message}`")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Wyślij wiadomość powitania"""
        guild_id = str(member.guild.id)
        if guild_id in self.config and "welcome_message" in self.config[guild_id]:
            channel = member.guild.system_channel
            if channel:
                message = self.config[guild_id]["welcome_message"].replace("{user}", member.mention)
                await channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Wyślij wiadomość pożegnania"""
        guild_id = str(member.guild.id)
        if guild_id in self.config and "goodbye_message" in self.config[guild_id]:
            channel = member.guild.system_channel
            if channel:
                message = self.config[guild_id]["goodbye_message"].replace("{user}", member.name)
                await channel.send(message)

async def setup(bot):
    await bot.add_cog(Welcome(bot))

