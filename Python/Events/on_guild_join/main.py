import discord

token = "token"
id = 123456789 #channel id

bot = discord.Client()

@bot.event
async def on_guild_join(guild):
	embed = discord.Embed(title="New guild",color=0x00FF00)
	embed.add_field(name="Name",value=guild.name,inline=False)
	embed.add_field(name="Owner",value=guild.owner,inline=False)
	embed.add_field(name="Member count",value=guild.member_count,inline=False)
	channel = bot.get_channel(id)
	await channel.send(embed=embed)

bot.run(token)
