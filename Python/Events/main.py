import discord
import time

token = "token"
prefix = "!"

bot = discord.Client()

@bot.event
async def on_ready():
	print(f'''Logged in as {bot.user} ({bot.user.id})
I am on {len(bot.guilds)} servers''')

bot.run(token)
