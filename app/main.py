import os
import dotenv
from server import server_thread
import discord
from discord import app_commands

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.all()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# botのログインと同期
@bot.event
async def on_ready():
    print('ログインしました')

    # アクティビティを設定
    game = discord.Game("helpコマンドでbotの使い方をお伝えします。")
    await bot.change_presence(status=discord.Status.idle, activity=game)

    # スラッシュコマンドを同期
    await tree.sync()

# スラッシュコマンドを設定
@tree.command(name='test', description='Say hello to the world!') 
async def test(interaction: discord.Interaction): 
    await interaction.response.send_message('Hello, World!')

# トークンを指定してbot実行
server_thread()
bot.run(TOKEN)