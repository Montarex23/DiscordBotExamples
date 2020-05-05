import discord

token = "token"

bot = discord.Client()

@bot.event
async def on_message_edit(before, after):
	if before.content == after.content:
		return
		
	embed = discord.Embed(title="Message edited",color=0x00FF00)
	embed.add_field(name="Message author",value=after.author,inline=False)
	embed.add_field(name="Before",value=before.content,inline=False)
	embed.add_field(name="After",value=after.content,inline=False)
	await after.channel.send(embed=embed)

bot.run(token)
