import discord
from discord.ext import commands

class Battle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # create a command
    async def hello(self, ctx): # all methods now must have both self and ctx parameters
        print("invoked") 
        await ctx.send('Hello!')

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send('Goodbye!')

    @discord.slash_command() # we can also add application commands
    async def hello(self, ctx):
        await ctx.respond('Hello!')

    @discord.slash_command()
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

def setup(bot):
    bot.add_cog(Battle(bot))
    print("Battle system succesfully loaded")
