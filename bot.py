import discord
from discord.ext import commands
import json
import os
from datetime import datetime

with open('./config.json', 'r') as f:
    config = json.load(f)
#kadirstudio tarafından kodlandı.
prefix = config.get('prefix', '!')
TOKEN = config.get('token', '')

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.event
async def on_ready():
    print(f'[{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}] Bot {bot.user.name} olarak giriş yaptı!')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')
        print(f'[+] {filename} komutu başarıyla yüklendi.')

for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')
        print(f'[+] {filename} eventi başarıyla yüklendi.')

bot.run(TOKEN)
