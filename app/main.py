import os
import dotenv
from server import server_thread
import discord
from discord import app_commands
from commands import HelloCog

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

# @tree.command(name='hello', description='Say hello to the world!') 
# async def test(interaction: discord.Interaction): 
#   await interaction.response.send_message('Hello, World!')

# トークンを指定してbot実行
server_thread()
client.add_cog(HelloCog(client))
client.run(TOKEN)