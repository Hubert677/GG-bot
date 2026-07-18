import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, interaction: discord.Interaction):
        return interaction.user.guild_permissions.administrator

    @app_commands.command(name='ban', description='Zbanuj użytkownika (ADMIN)')
    async def ban(self, interaction: discord.Interaction, member: discord.User, reason: str = "Brak podanego powodu"):
        """Zbanuj użytkownika (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return

        try:
            await interaction.guild.ban(member, reason=reason)
            embed = discord.Embed(
                title="🔨 Użytkownik Zbanowany",
                description=f"**Użytkownik:** {member.mention}\n**Powód:** {reason}",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Błąd: {e}", ephemeral=True)

    @app_commands.command(name='kick', description='Wyrzuć użytkownika (ADMIN)')
    async def kick(self, interaction: discord.Interaction, member: discord.User, reason: str = "Brak podanego powodu"):
        """Wyrzuć użytkownika (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return

        try:
            await interaction.guild.kick(member, reason=reason)
            embed = discord.Embed(
                title="👢 Użytkownik Wyrzucony",
                description=f"**Użytkownik:** {member.mention}\n**Powód:** {reason}",
                color=discord.Color.orange()
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Błąd: {e}", ephemeral=True)

    @app_commands.command(name='warn', description='Ostrzeż użytkownika (ADMIN)')
    async def warn(self, interaction: discord.Interaction, member: discord.User, reason: str = "Brak podanego powodu"):
        """Ostrzeż użytkownika (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return

        embed = discord.Embed(
            title="⚠️ Ostrzeżenie",
            description=f"**Użytkownik:** {member.mention}\n**Powód:** {reason}\n**Ostrzegł:** {interaction.user.mention}",
            color=discord.Color.yellow()
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='clear', description='Usuń wiadomości (ADMIN)')
    async def clear(self, interaction: discord.Interaction, amount: int = 10):
        """Usuń wiadomości (ADMIN)"""
        if not self.is_admin(interaction):
            await interaction.response.send_message("❌ Brak uprawnień! Tylko admin może to robić.", ephemeral=True)
            return

        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"✅ Usunięto {len(deleted)} wiadomości.", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))

