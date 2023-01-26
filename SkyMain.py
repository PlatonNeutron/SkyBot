import discord
from discord import app_commands

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
base = app_commands.CommandTree(bot)


# Main part of the bot
@bot.event
async def on_ready():
    await base.sync(guild=discord.Object(id=362272596517191691))
    print(f'{bot.user} has successfuly connected to Discord')

#Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.                                 
@base.command(name = "config_wip", description = "To config the bot", guild=discord.Object(id=362272596517191691))
async def first_command(interaction):
    await interaction.response.send_message("WIP")

@base.command(name = "shutdown", description = "Shutdown the bot", guild=discord.Object(id=362272596517191691)) 
async def shutdown(interaction):
    if interaction.user.id == 286827468445319168:
        print(f'{bot.user} has been successfuly shutdown')
        await bot.close()

# Skyblock commands part
@base.command(name = "évènements_wip", description = "A list of all the events this week", guild=discord.Object(id=362272596517191691))
async def first_command(interaction):
    await interaction.response.send_message("WIP")

@base.command(name = "maire_wip", description = "To see the current mayor and perks", guild=discord.Object(id=362272596517191691))
async def first_command(interaction):
    await interaction.response.send_message("WIP")

bot.run('')