@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "Reason Not Provided"):
  await member.send("You Have Been kicked from Server, Because: "+reason)
  await member.kick(reason=reason)