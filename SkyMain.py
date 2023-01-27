import requests

import discord
from discord import app_commands

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
base = app_commands.CommandTree(bot)
hypixelApiOAuth = {'Authorization' : 'Bearer {1f49f071-cf58-4f77-a710-5f4a8ae06c7a}'}


# Main part of the bot
@bot.event
async def on_ready():
    await base.sync(guild=discord.Object(id=362272596517191691))
    print(f'{bot.user} has successfuly connected to Discord')

#Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.                                 
@base.command(name = "config_wip", description = "To config the bot", guild=discord.Object(id=362272596517191691))
async def config(interaction):
    await interaction.response.send_message("WIP")

@base.command(name = "shutdown", description = "Shutdown the bot", guild=discord.Object(id=362272596517191691)) 
async def shutdown(interaction):
    if interaction.user.id == 286827468445319168:
        print(f'{bot.user} has been successfuly shutdown')
        await bot.close()

# Skyblock commands part
@base.command(name = "events_wip", description = "A list of all the events this week", guild=discord.Object(id=362272596517191691))
async def events(interaction):
    await interaction.response.send_message("WIP")

@base.command(name = "mayor_wip", description = "To see the current mayor and perks", guild=discord.Object(id=362272596517191691))
async def mayor(interaction):
    hypixelApiRequest = requests.get('https://api.hypixel.net/resources/skyblock/election', headers=hypixelApiOAuth)
    request = hypixelApiRequest.json()
    getCurrentMayor = request["mayor"]["name"]

    electionEmbed = discord.Embed(title="Test", description="test")

    if(getCurrentMayor == "Aatrox"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Aatrox_Sprite.webp")
    elif(getCurrentMayor == "Cole"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Cole_Sprite.webp")
    elif(getCurrentMayor == "Derpy"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Derpy_Sprite.webp")
    elif(getCurrentMayor == "Diana"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Diana_Sprite.webp")
    elif(getCurrentMayor == "Diaz"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Diaz_Sprite.webp")
    elif(getCurrentMayor == "Finnegan"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Finnegan_Sprite.webp")
    elif(getCurrentMayor == "Foxy"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Foxy_Sprite.webp")
    elif(getCurrentMayor == "Jerry"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Jerry_Sprite.webp")
    elif(getCurrentMayor == "Marina"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Marina_Sprite.webp")
    elif(getCurrentMayor == "Paul"):
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Paul_Sprite.webp")
    else:
        electionEmbed.set_thumbnail(url="https://raw.githubusercontent.com/PlatonNeutron/SkyBot/main/assets/mayor/Scorpius_Sprite.webp")
    
    await interaction.response.send_message(embed=electionEmbed)

bot.run('MTA2ODEyOTIzNzU5MDA5Mzg5NA.GnSfiA.KApS_OU3v729tiwvKn1-NBrAjQasyw6eRKHi7g')