import discord
import json

def VerItensPlayer(client, GUILDS):
  @client.command(name="player", guild_ids=GUILDS)
  async def players_(ctx, user: discord.Member):
    JFile = json.load(open('files/Listings.json'))
    if not str(user.id) in JFile or len(JFile[str(user.id)]) == 0:
      return await ctx.respond(":no_entry: Erro: `Este usuário não possui nenhuma listing.`", ephemeral=True)
    listingStr = ""
    for listing in JFile[str(user.id)]:
      listingStr += f":pushpin: **{listing['item']}** - :moneybag: {listing['coins']} coins | :receipt: Quantidade: `{listing['quantidade']}`\n"
    await ctx.respond(f"{user.mention} possui as seguintes listings:\n{listingStr}")