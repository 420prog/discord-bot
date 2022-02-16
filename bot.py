from discord.ext import commands
from dotenv import load_dotenv

import os

load_dotenv()

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
	print("Bot jest gotowy!")

@bot.command()
async def pomoc(ctx: commands.Context):
	await ctx.send("Twoja treść")
  
@bot.command()
async def komendy(ctx: commands.Context):
	await ctx.send("!pomoc   !komendy")

bot.run(os.eviron['TOKEN'])
#autor TheOnlyBen#0001
