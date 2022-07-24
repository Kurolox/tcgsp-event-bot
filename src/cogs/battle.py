import discord
from discord import Option, SlashCommandOptionType
from discord.ext import commands
from controllers import tamer

class ChallengeView(discord.ui.View):
    @discord.ui.button(label="Aceptar", style=discord.ButtonStyle.green) 
    async def accept_challenge(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

    @discord.ui.button(label="Rechazar", style=discord.ButtonStyle.red) 
    async def decline_challenge(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

class Battle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.commands.slash_command(
        name="retar",
        description="Reta a un tamer en el servidor para obtener sus {ALEX INSERTAME ALGO AQUI PLS}"
    )
    async def challenge(
        self, 
        ctx: discord.ApplicationContext,
        defender: Option(SlashCommandOptionType.user, "Escoge al tamer a quien quieres retar", name="usuario"),
        bet: Option(SlashCommandOptionType.integer, "Escoge la cantidad de {ALEX INSERTAME ALGO} que quieres apostar", name="cantidad")
    ):
        # Sanity check to see if the user is challenging himself
        if (ctx.user == defender):
            return await ctx.respond("Aprecio tu entusiasmo, pero retarte a ti mismo no va a cambiar tu cantidad de {ALGO ALEX} ganes o pierdas, no crees?", ephemeral=True)

        # Check if the attacker meets all of the needed conditions
        attacker_tamer = tamer.get(ctx.user)
        if (attacker_tamer.in_battle):
            return await ctx.respond("Parece ser que ya estas en medio de un reto. Termina el reto actual antes de empezar uno nuevo!", ephemeral=True)
        if (attacker_tamer.currency < bet):
            return await ctx.respond("No tienes suficiente {ALEX DAME UN NOMBRE} para cubrir el reto.", ephemeral=True)

        # Check if the defender meets all of the needed conditions
        defender_tamer = tamer.get(defender)
        if (defender_tamer.in_battle):
            return await ctx.respond("La persona a la que estas retando ya tiene un reto en curso. Vas a tener que esperar a que termine.", ephemeral=True)
        if (defender_tamer.currency < bet):
            return await ctx.respond("La persona a la que estas retando no tiene suficiente {ALEX TE QUEREMOS} para el reto!", ephemeral=True)

        # At this point the challenge declaration is valid, send a message to get
        # the defender tamer's approval of the challenge
        await ctx.respond(f"""<@{defender.id}>, has sido retado por <@{ctx.user.id}> poniendo {bet} ALGO en linea! Reacciona a este mensaje para confirmar o declinar el reto.
        
        Si el reto no es confirmado tras 10 minutos, este sera rechazado automaticamente.""", delete_after=600, view=ChallengeView())


def setup(bot):
    bot.add_cog(Battle(bot))
    print("Battle system succesfully loaded")