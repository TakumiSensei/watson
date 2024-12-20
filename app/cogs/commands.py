import discord
from discord.ext import commands
from discord import app_commands
import random

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog準備完了")
	
    @app_commands.command(name="hello", description='Say hello to the world!')
    async def hello(self, interaction:discord.Interaction):
        await interaction.response.send_message('Hello, World!')

    @app_commands.command(name="dice", description="ダイスを振ります。")
    @app_commands.describe(list="カンマ区切りで項目を入力して下さい。")
    async def dice(self, interaction:discord.Interaction, list:str):
        dicelist = list.split(',')
        await interaction.response.send_message(f"「{list}」の中から抽選します。\n選ばれたのは、** 「{str(random.choice(dicelist))}」**です！")

async def setup(bot):
    await bot.add_cog(BasicCog(bot))