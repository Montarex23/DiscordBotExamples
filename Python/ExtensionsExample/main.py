import discord
from discord.ext import commands
import traceback

token = "token"

def get_prefix(bot, message):
	prefix = "!"
	return commands.when_mentioned_or(prefix)(bot, message)

initial_extensions = ['cogs.cog1',
'cogs.cog2']

bot = commands.Bot(command_prefix=get_prefix,case_insensitive=True)
bot.remove_command('help')

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except:
			print("-" * 100)
			print(f"ERROR when loading {extension}:\n")
			traceback.print_exc()
			
@bot.event
async def on_ready():
	print('Logged in')
	
@bot.event
async def on_message(message):
	if message.author.bot:
		return
	# If you want do sth every message
	await bot.process_commands(message)

bot.run(token)
