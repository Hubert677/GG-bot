import discord
from discord.ext import commands
from discord import app_commands
import json
import os

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "roles_config.json"
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

    @app_commands.command(name="role-add", description="Dodaj rolę użytkownikowi (ADMIN)")
    async def role_add(self, interaction: discord.Interaction, user: discord.User, role: str):
        """Dodaj rolę użytkownikowi"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień!", ephemeral=True)
            return
        
        try:
            member = await interaction.guild.fetch_member(user.id)
            role_obj = discord.utils.find(lambda r: r.name.lower() == role.lower(), interaction.guild.roles)
            
            if not role_obj:
                await interaction.response.send_message(f"❌ Rola '{role}' nie istnieje!", ephemeral=True)
                return
            
            await member.add_roles(role_obj)
            embed = discord.Embed(
                title="✅ Rola Dodana",
                description=f"**Użytkownik:** {user.mention}\n**Rola:** {role_obj.mention}",
                color=discord.Color.green()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Błąd: {e}", ephemeral=True)

    @app_commands.command(name="role-remove", description="Usuń rolę użytkownikowi (ADMIN)")
    async def role_remove(self, interaction: discord.Interaction, user: discord.User, role: str):
        """Usuń rolę użytkownikowi"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień!", ephemeral=True)
            return
        
        try:
            member = await interaction.guild.fetch_member(user.id)
            role_obj = discord.utils.find(lambda r: r.name.lower() == role.lower(), interaction.guild.roles)
            
            if not role_obj:
                await interaction.response.send_message(f"❌ Rola '{role}' nie istnieje!", ephemeral=True)
                return
            
            await member.remove_roles(role_obj)
            embed = discord.Embed(
                title="✅ Rola Usunięta",
                description=f"**Użytkownik:** {user.mention}\n**Rola:** {role_obj.mention}",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Błąd: {e}", ephemeral=True)

    @app_commands.command(name="role-list", description="Pokaż wszystkie role na serwerze")
    async def role_list(self, interaction: discord.Interaction):
        """Pokaż role na serwerze"""
        roles = [role for role in interaction.guild.roles if role.name != "@everyone"]
        
        if not roles:
            await interaction.response.send_message("❌ Brak roli na serwerze!", ephemeral=True)
            return
        
        roles_str = "\n".join([f"• {role.mention}" for role in roles[:20]])
        
        embed = discord.Embed(
            title="🏷️ Role na Serwerze",
            description=roles_str if roles_str else "Brak roli",
            color=discord.Color.blue()
        )
        embed.set_footer(text=f"Razem roli: {len(roles)}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="myroles", description="Pokaż swoje role")
    async def myroles(self, interaction: discord.Interaction):
        """Pokaż swoje role"""
        member = await interaction.guild.fetch_member(interaction.user.id)
        roles = [role for role in member.roles if role.name != "@everyone"]
        
        if not roles:
            await interaction.response.send_message("Nie masz żadnych roli!", ephemeral=True)
            return
        
        roles_str = "\n".join([f"• {role.mention}" for role in roles])
        
        embed = discord.Embed(
            title="🏷️ Twoje Role",
            description=roles_str,
            color=discord.Color.purple()
        )
        embed.set_footer(text=f"Razem roli: {len(roles)}")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Roles(bot))
