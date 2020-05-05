import discord

token = "token"

bot = discord.Client()

@bot.event
async def on_message(message):
	print(f'''Message ID: {message.id}
Message Content: {message.content}
Message Channel: {message.channel}
Message Channel ID: {message.channel.id}
Message Channel Name: {message.channel.name}
Message Channel Position: {message.channel.position}
Message Channel NSFW: {message.channel.nsfw}
Message Channel Category ID: {message.channel.category_id}
Message Channel Type: {message.channel.type}
Message Author: {message.author}
Message Author ID: {message.author.id}
Message Author Name: {message.author.name}
Message Author Discriminator: {message.author.discriminator}
Message Author Bot: {message.author.bot}
Message Author Nick: {message.author.nick}
Message Guild: {message.guild}
Message Guild ID: {message.guild.id}
Message Guild Name: {message.guild.name}
Message Guild Shard ID: {message.guild.shard_id}
Message Guild Chunked: {message.guild.chunked}
Message Guild Member Count: {message.guild.member_count}
Message Flags Value: {message.flags.value}''')

bot.run(token)
