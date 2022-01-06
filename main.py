import discord  # Imports the discord module.
from discord.ext import commands  # Imports discord extensions.

# The below code verifies the "client".

client = commands.Bot(command_prefix='!')
# The below code stores the token.
token = "OTI4Mzc0NTI5MDQ5MzYyNDg0.YdX2KA.on4tTvkZdy458hZU30ItbJiWOzQ"

'''The below code displays if you have any errors publicly. This is useful if you don't want to display them in your 
output shell. '''


@client.event
@commands.has_permissions(administrator=True)
async def on_message(message):
    if message.author.guild_permissions.administrator:
        if message.content.startswith("https:"):
            await message.delete()
        if message.content.startswith("discord.gg/"):
            await message.delete()
    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Bitte nutze folgendes Schema: !befehl @User Grund.')
        await ctx.message.delete()
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Du bist dazu nicht berechtigt!")
        await ctx.message.delete()


# The below code bans player.
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member is None:
        await ctx.send("Gebe einen User an, der gebannt werden soll.")
        await ctx.message.delete()
        return
    elif reason is None:
        await ctx.send("Gebe eine Begründung für den Bann an.")
        await ctx.message.delete()
        return
    await member.ban(reason=reason)
    await ctx.message.delete()
    embed = discord.Embed(title="Bann", description=f"{member.mention} wurde wegen {reason} gebannt.",
                          color=discord.Color.dark_red())
    await ctx.send(embed=embed)


# The below code unbans player.
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} wurde entbannt.')
            return
    await ctx.message.delete()


# The below code kicks player
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member is None:
        await ctx.send("Gebe einen User an, der gekickt werden soll.")
        await ctx.message.delete()
        return
    elif reason is None:
        await ctx.send("Gebe eine Begründung für den Kick an.")
        await ctx.message.delete()
        return
    await member.kick(reason=reason)
    await ctx.message.delete()
    embed = discord.Embed(title="Kick", description=f"{member.mention} wurde wegen {reason} gekickt.",
                          color=discord.Color.dark_red())
    await ctx.send(embed=embed)


@client.command()
async def embed(ctx, title=None, *, description=None):
    embed = discord.Embed(title=title, description=description, color=discord.Color.blue())  # ,color=Hex code
    await ctx.send(embed=embed)
    await ctx.message.delete()


# The below code runs the bot.
client.run(token)
