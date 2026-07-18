import discord
from discord.ext import commands
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

    def is_admin(self, ctx):
        return ctx.author.guild_permissions.administrator

    @commands.command(name='set-welcome')
    async def set_welcome(self, ctx, *, message):
        """Ustaw wiadomość powitania dla nowych użytkowników (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return
        
        guild_id = str(ctx.guild.id)
        self.config[guild_id] = self.config.get(guild_id, {})
        self.config[guild_id]["welcome_message"] = message
        self.save_config()
        await ctx.send(f"✅ Wiadomość powitania ustawiona:\n`{message}`")

    @commands.command(name='set-goodbye')
    async def set_goodbye(self, ctx, *, message):
        """Ustaw wiadomość pożegnania dla użytkowników (ADMIN)"""
        if not self.is_admin(ctx):
            await ctx.send("❌ Brak uprawnień! Tylko admin może to robić.")
            return
        
        guild_id = str(ctx.guild.id)
        self.config[guild_id] = self.config.get(guild_id, {})
        self.config[guild_id]["goodbye_message"] = message
        self.save_config()
        await ctx.send(f"✅ Wiadomość pożegnania ustawiona:\n`{message}`")

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
