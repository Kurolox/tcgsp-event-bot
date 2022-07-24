from unicodedata import name
import discord
from discord import Option, SlashCommandOptionType
from discord.ext import commands

class Battle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Only used for recovering the Guild ID, this command should be deleted
    @commands.command() 
    async def get_guild_id(self, ctx): 
        print(f"Guild ID recovered: {ctx.guild.id}") 

    @discord.commands.slash_command(
        name="retar",
        description="Reta a un tamer en el servidor para obtener sus {ALEX INSERTAME ALGO AQUI PLS}"
    )
    async def challenge(
        self, 
        ctx: discord.ApplicationContext,
        defender: Option(SlashCommandOptionType.user, "Escoge al tamer a quien quieres retar", name="usuario"),
        bet: Option(SlashCommandOptionType.number, "Escoge la cantidad de {ALEX INSERTAME ALGO} que quieres apostar", name="cantidad")
    ):
        await ctx.respond('Goodbye')

def setup(bot):
    bot.add_cog(Battle(bot))
    print("Battle system succesfully loaded")