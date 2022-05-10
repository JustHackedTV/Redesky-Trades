import discord
import json

def procurar(client, GUILDS):
  @client.command(name="procurar", guild_ids=GUILDS)
  async def procurar_(ctx, item: discord.Option(str, default=None, required=False)):
    if item == None:
      return await ctx.respond(":no_entry: Erro: `Você não informou o item.`", ephemeral=True)
    JFile = json.load(open('files/Items.json'))
    if str(item) not in JFile:
      return await ctx.respond(":no_entry: Erro: `Não há alguem vendendo esse item.`", ephemeral=True)
    ListingString = ""
    for i in JFile[str(item)]:
      coinSimplfied = 0
      if i['coins'] >= 1000000000:
        coinSimplfied = f"${int(i['coins'] / 1000000000)}b (bilhões)"
      elif i['coins'] >= 1000000:
        coinSimplfied = f"${int(i['coins'] / 1000000)}kk (milhões)"
      elif i['coins'] >= 1000:
        coinSimplfied = f"${int(i['coins'] / 1000)}k"
      elif i['coins'] >= 1:
        coinSimplfied = f"${int(i['coins'])}"
      ListingString += f":moneybag: **Coins**: `{coinSimplfied}` - :receipt: **Quantidade**: `{i['quantidade']}`\n:man_detective: **Dono**: <@{i['dono']}>\n\n"
    embed = discord.Embed(title=f"Listings de '{item}'", description=ListingString, color=0xe3d21b)
    await ctx.respond(content=ctx.author.mention, embed=embed)