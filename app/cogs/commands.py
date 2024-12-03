import discord
from discord.ext import commands
from discord import app_commands

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog準備完了")
	
    @app_commands.command(name="hello", description='Say hello to the world!')
    async def hello(self, interaction:discord.Interaction):
        await interaction.response.send_message('Hello, World!')

    @app_commands.command(name="dice", description="ダイスを振ります")
    async def dice(self, interaction:discord.Interaction, *args):
        arguments = ', '.join(args)
        await interaction.response.send_message(f"ダイス結果は, {arguments}")

async def setup(bot):
    await bot.add_cog(BasicCog(bot))