import discord
from discord.ext import commands
import Commands
import Date
import Events


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('$help'))
    print('Bot online'.format(client))


@client.command(pass_context=True)
async def random(ctx, numar, number):
    await Commands.random(ctx, numar, number)


@client.command(pass_context=True)
async def coinflip(ctx):
    await Commands.coinflip(ctx)


@client.command(pass_context = True)
async def zar(ctx):
    await Commands.zar(ctx)


@client.command(pass_context = True)
async def membrii(ctx):
    await Commands.membrii(ctx)


@client.command(pass_context = True)
async def join(ctx):
    await Commands.join(ctx)
    

@client.command(pass_context = True)
async def leave(ctx):
    await Commands.leave(ctx)


@client.event
async def on_message(message):
    string_split=message.content.split(" ")
    if message.content.startswith('$hello'):
        await Events.hello(message)
        return
    if message.content.startswith('$goodbye'):
        await Events.goodbye(message)
        return
    if message.content.startswith('$tts'):
        await Events.tts(message, string_split, client)
        return
    if message.content.startswith('$set'):
        await Events.set(message, string_split)
        return
    if message.content.startswith('$help'):
        await Events.help(message)
        return
    if message.content.startswith('$alege'):
        await Events.alege(message, message.content)
        return
    await client.process_commands(message)
    if message.author == client.user:
        return
    

client.run(Date.token)