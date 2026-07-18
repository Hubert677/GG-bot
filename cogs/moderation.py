import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command(name='ban')
    async def ban(self, ctx, member: discord.Member, *, reason="Brak podanego powodu"):
        """Zbanuj użytkownika (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return

        try:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title="🔨 Użytkownik Zbanowany",
                description=f"**Użytkownik:** {member.mention}\n**Powód:** {reason}",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"❌ Błąd: {e}")

    @commands.command(name='kick')
    async def kick(self, ctx, member: discord.Member, *, reason="Brak podanego powodu"):
        """Wyrzuć użytkownika (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return

        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                title="👢 Użytkownik Wyrzucony",
                description=f"**Użytkownik:** {member.mention}\n**Powód:** {reason}",
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f"❌ Błąd: {e}")

    @commands.command(name='warn')
    async def warn(self, ctx, member: discord.Member, *, reason="Brak podanego powodu"):
        """Ostrzeż użytkownika (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return

        embed = discord.Embed(
            title="⚠️ Ostrzeżenie",
            description=f"**Użytkownik:** {member.mention}\n**Powód:** {reason}\n**Ostrzegł:** {ctx.author.mention}",
            color=discord.Color.yellow()
        )
        await ctx.send(embed=embed)

    @commands.command(name='clear')
    async def clear(self, ctx, amount: int = 10):
        """Usuń wiadomości (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return

        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"✅ Usunięto {len(deleted)} wiadomości.", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
