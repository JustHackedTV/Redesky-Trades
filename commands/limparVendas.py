import discord
import json

def limparVendas(client, GUILDS):
  @client.command(name="limpar", guild_ids=GUILDS)
  async def limpar_(ctx):
    JFile = json.load(open('files/Listings.json'))
    if str(ctx.author.id) not in JFile or len(JFile[str(ctx.author.id)]) == 0:
      return await ctx.respond(":no_entry: Erro: `Você não possui nenhuma listing.`", ephemeral=True)
    IJFile = json.load(open('files/Items.json'))
    for listing in JFile[str(ctx.author.id)]:
      if listing['item'] not in IJFile:
        pass
      else:
        for i in IJFile[listing['item']]:
          if i['dono'] == str(ctx.author.id):
            IJFile[listing['item']].remove(i)
    json.dump(IJFile, open('files/Items.json', 'w'))
    JFile[str(ctx.author.id)] = []
    json.dump(JFile, open('files/Listings.json', 'w'))
    await ctx.respond(":broom: Listings limpas com sucesso!")
