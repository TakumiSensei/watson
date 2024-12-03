import discord
from discord.ext import commands
from discord import app_commands

class HelloCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog ready!")
	
    @app_commands.command(name="hello", description='Say hello to the world!')
    async def hello(self,interaction:discord.Interaction):
        await interaction.response.send_message('Hello, World!')

async def setup(bot):
    await bot.add_cog(HelloCog(bot))