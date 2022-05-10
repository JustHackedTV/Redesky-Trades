import discord
import json

Info = json.load(open('BotInfo.json'))
TOKEN = Info['Token']
GUILDS = Info['GUILDS']

client = discord.Bot()

#EVENTS
@client.event
async def on_ready():
    print('{} is ready!'.format(client.user.name))

#IMPORT COMMANDS
from commands.createListing import CreateListing
CreateListing(client, GUILDS)
from  commands.verItensPlayer import VerItensPlayer
VerItensPlayer(client, GUILDS)
from commands.limparVendas import limparVendas
limparVendas(client, GUILDS)

client.run(TOKEN)