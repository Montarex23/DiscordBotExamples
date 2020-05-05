import discord

token = "token"
prefix = "!"

bot = discord.Client()

@bot.event
async def on_message(message):
	if message.author.bot:
		return
		
	if message.content.lower().startswith(prefix + "game "):
		game = message.content[len(prefix)+5:]
		await bot.change_presence(activity=discord.Game(name=game))
		await message.channel.send(f"Game changed to **{game}**")

bot.run(token)
