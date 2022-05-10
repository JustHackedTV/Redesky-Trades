import discord
import json

def CreateListing(client, GUILDS):
  @client.command(name="listar", guild_ids=GUILDS)
  async def listar_(ctx, item: discord.Option(str, default=None, required=False), coins: discord.Option(int, default=None, required=False), quantidade: discord.Option(int, default=None, required=False)):
    if coins == None:
      return await ctx.respond(":no_entry: Erro: `Você não informou o número de coins.`", ephemeral=True)
    if item == None:
      return await ctx.respond(":no_entry: Erro: `Você não informou o item.`", ephemeral=True)
    if coins < 0:
      return await ctx.respond(":no_entry: Erro: `Você não pode colocar um número negativo de coins.`", ephemeral=True)
    if quantidade < 0 or quantidade == None:
      return await ctx.respond("Erro: `Você não pode colocar um número negativo ou nulo de quantidade.`", ephemeral=True)
    JFile = json.load(open('files/Listings.json'))
    if not str(ctx.author.id) in JFile:
      JFile[str(ctx.author.id)] = []
    JFile[str(ctx.author.id)].append({'item': item, 'coins': coins, 'quantidade': quantidade})
    json.dump(JFile, open('files/Listings.json', 'w'))
    embed = discord.Embed(title="Listing criada com sucesso!", description=f":pushpin: **Item**: `{item}`\n:moneybag: **Coins**: `{coins}`\n:receipt: **Quantidade**: `{quantidade}`", color=0x00ff00)
    await ctx.respond(content=ctx.author.mention + " - :round_pushpin: Listing criada com sucesso!", embed=embed, ephemeral=True)