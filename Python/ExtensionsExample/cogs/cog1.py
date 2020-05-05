import discord
from discord.ext import commands
import time

class Cog1(commands.Cog):
	"""Cog1"""

	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name="ping", aliases=['botping','pingbot'])
	async def pingcmd(self, ctx):
		before = time.monotonic()
		botmsg = await ctx.send("Pong!")
		ping = (time.monotonic() - before) * 1000
		await botmsg.edit(content=f":ping_pong: Gateway: {str(self.bot.latency*1000).split('.')[0]}ms\n:ping_pong: Bot: {int(ping)}ms")

	@commands.command(name="hello")
	async def hellocmd(self, ctx):
		await ctx.send("Hello!")

def setup(bot):
    bot.add_cog(Cog1(bot))
