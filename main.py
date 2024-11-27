import discord
from discord import app_commands
import config
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# botのログインと同期
@client.event
    async def on_ready():
    print('ログインしました')