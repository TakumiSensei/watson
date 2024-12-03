import os
import dotenv
from server import server_thread
import discord
from discord.ext import commands

dotenv.load_dotenv()

INITIAL_EXTENSIONS = [
    'cogs.commands'
]
TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
# bot = discord.Client(intents=intents)
# tree = app_commands.CommandTree(bot)

# botのログインと同期
@bot.event
async def on_ready():
    print('ログインしました')

    # アクティビティを設定
    game = discord.Game("helpコマンドでbotの使い方をお伝えします。")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    
    for cog in INITIAL_EXTENSIONS:
        await bot.load_extension(cog)

    # スラッシュコマンドを同期
    await bot.tree.sync()

# @tree.command(name='hello', description='Say hello to the world!') 
# async def test(interaction: discord.Interaction): 
#   await interaction.response.send_message('Hello, World!')

# トークンを指定してbot実行
server_thread()
bot.run(TOKEN)