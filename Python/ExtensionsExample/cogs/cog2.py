import discord
from discord.ext import commands
import time

class Cog2(commands.Cog):
	"""Cog2"""

	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name="hotel")
	async def hotelcmd(self, ctx):
		await ctx.send("Trivago")
		
	@commands.command(name="say")
	async def saycmd(self, ctx, *text):
		text = " ".join(text)
		await ctx.send(text)

def setup(bot):
    bot.add_cog(Cog2(bot))
