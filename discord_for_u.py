import discord
from discord.ext import commands
from discord import utils
from discord.utils import get
PREFIX = '!' #prefix for u'r bot
client = commands.Bot( command_prefix = PREFIX )
@client.event()
async def on_ready():
    print('bot connected')
@client.command()
@commands.has_permissions(administrator = True) #permissions for the command
async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.message.delete() #delete message with command
    await member.kick(reason = reason) #kick
    await ctx.send(f'{member.mention} was kicked from this server!')#bots message about kick
    #example for the command (!kick @kiozet)
@client.command()
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.ban(reason = reason) #ban member
    await ctx.send(f'{member.mention} was banned on this server!')#bots message about ban
    #example (!ban @kiozet)
@client.command()
@commands.has_permissions( administrator = True )
async def mute(ctx, member: discord.Member):
    await ctx.message.delete()
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'muted') #bot find this role
    #for this command u need to create new role "muted", wich won't have permissions to talk in the voice
    await member.add_roles( mute_role )  #bot find this role
    await ctx.send(f'{member.mention} was muted.')
    #example for the command (!mute @kiozet)
@client.command()
@commands.has_permissions(administrator = True)
async def unmute(ctx, member: discord.Member):
    await ctx.message.delete()
    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'muted') #bot find this role
    await member.remove_roles( mute_role )  #bot remove role from the member
    await ctx.send(f'{member.mention} was unmuted.')
    #example for the command (!unmute @kiozet)
client.run('your token') #starting u'r bot
