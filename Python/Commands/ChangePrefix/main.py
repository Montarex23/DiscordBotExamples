import discord
from discord.ext import commands
import pickledb


token = "token"

bot = discord.Client()

@bot.event
async def on_message(message):
	config = pickledb.load('prefix.db', False)
	if config.get(str(message.guild.id)) not in [False, None]:
		prefix = config.get(str(message.guild.id))
	else:
		prefix = '!'
	del config
		
	if message.author.bot:
		return
	
	if message.content.lower() == prefix + "hello":
		await message.channel.send('Hello!')
	
	if message.content.lower().startswith(prefix+'prefix '):
		new_prefix = message.content[len(prefix)+7:]
		config = pickledb.load('prefix.db', False)
		config.set(str(message.guild.id), new_prefix)
		config.dump()
		await message.channel.send(f"Prefix changed to **{new_prefix}**")
		del config
			
	
bot.run(token)
