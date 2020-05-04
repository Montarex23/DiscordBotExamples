import discord
import time

token = "token"
prefix = "!"

bot = discord.Client()

@bot.event
async def on_message(message):
	if message.author.bot:
		return
		
	if message.content.lower() == prefix + "ping":
		before = time.monotonic()
		botmsg = await message.channel.send("Pong!")
		ping = (time.monotonic() - before) * 1000
		await botmsg.edit(content=f":ping_pong: Gateway: {str(bot.latency*1000).split('.')[0]}ms\n:ping_pong: Bot: {int(ping)}ms")

bot.run(token)
