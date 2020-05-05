import discord

token = "token"

bot = discord.Client()

@bot.event
async def on_message_delete(message):
	embed = discord.Embed(title="Message deleted", color=0xFF0000)
	embed.add_field(name="Message author",value=message.author,inline=False)
	embed.add_field(name="Message content",value=message.content,inline=False)
	await message.channel.send(embed=embed)

bot.run(token)
