import discord
import json

def limparVendas(client, GUILDS):
  @client.command(name="limpar", guild_ids=GUILDS)
  async def limpar_(ctx):
    JFile = json.load(open('files/Listings.json'))
    if str(ctx.author.id) not in JFile or len(JFile[str(ctx.author.id)]) == 0:
      return await ctx.respond(":no_entry: Erro: `Você não possui nenhuma listing.`", ephemeral=True)
    JFile[str(ctx.author.id)] = []
    json.dump(JFile, open('files/Listings.json', 'w'))
    await ctx.respond(":broom: Listings limpas com sucesso!")