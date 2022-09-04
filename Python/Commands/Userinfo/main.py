import discord
import time

token = "token"
prefix = "!"

bot = discord.Client()

@bot.event
async def on_message(message):
	if message.author.bot:
		return
	
	if message.content.lower().startswith(prefix + "userinfo"):
		if len(message.mentions) == 1: #Mention
			user = bot.get_user(message.mentions[0].id)
		elif message.content[len(prefix)+9:] != "": #ID
			try:
				user = bot.get_user(int(message.content[len(prefix)+9:]))
			except:
				pass
		else: #Self
			user = message.author
		embed = discord.Embed(title=f"Information about {user}",color=message.author.color)
		embed.set_thumbnail(url=user.avatar.url)
		embed.add_field(name="ID",value=user.id,inline=False)
		created = user.created_at.__format__('%A, %d. %B %Y at %H:%M:%S')
		embed.add_field(name="Account creation",value=created, inline=False)
		member = message.guild.get_member(user.id)
		embed.add_field(name="Activity",value=member.activity,inline=False)
		embed.add_field(name="Avatar",value=f"[URL]({user.avatar.url})",inline=False)
		await message.channel.send(embed=embed)

bot.run(token)
