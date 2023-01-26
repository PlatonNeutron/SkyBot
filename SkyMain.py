import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
base = app_commands.CommandTree(bot)


# Main part of the bot
@bot.event
async def on_ready():
    await base.sync(guild=discord.Object(id=362272596517191691))
    print(f'We have logged in as {bot.user}')

#Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.                                 
@base.command(name = "config", description = "All the configs of the bots", guild=discord.Object(id=362272596517191691))
async def first_command(interaction):
    await interaction.response.send_message("... World!")

@base.command(name = "shutdown", description = "Shutdown the bot", guild=discord.Object(id=362272596517191691)) 
async def shutdown(interaction):
    if interaction.user.id == 286827468445319168:
        await bot.close()

# Skyblock commands part
@base.command(name = "hello", description = "My first application Command", guild=discord.Object(id=362272596517191691))
async def first_command(interaction):
    await interaction.response.send_message("... World!")

bot.run('')