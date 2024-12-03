import os
import dotenv
from server import server_thread
import discord
from discord import app_commands
import commands

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# botのログインと同期
@client.event
async def on_ready():
    print('ログインしました')

    # アクティビティを設定
    game = discord.Game("helpコマンドでbotの使い方をお伝えします。")
    await client.change_presence(status=discord.Status.idle, activity=game)

    # スラッシュコマンドを同期
    await tree.sync()

# トークンを指定してbot実行
server_thread()
client.run(TOKEN)