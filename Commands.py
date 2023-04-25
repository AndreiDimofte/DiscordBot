import random as rnd


async def random(ctx, numar, number):
    try:
        arg = rnd.randint(int(numar), int(number))
    except ValueError:
        await ctx.send("Numărul este invalid!")
    else:
        await ctx.send("Numărul random de la " + numar + " la " + number + " generat de " + ctx.author.mention + " este " +  "**" + str(arg) + "**" + "!")


determine_flip = [1, 0]
async def coinflip(ctx):    
    if rnd.choice(determine_flip) == 1:
        await ctx.send("Rezultatul generat de " + ctx.author.mention + " este " + "**" + "cap" + "**" + "!")
    else:
        await ctx.send("Rezultatul generat de " + ctx.author.mention + " este " + "**" + "pajură" + "**" + "!")


async def zar(ctx):
    try:
        sides = 6
        amount = 2
        rolls_list = []
        for number in range(int(amount)):
            rolls_list.append(rnd.randint(1, sides))
        await ctx.send("Zarurile aruncate de " + ctx.author.mention + " arată numerele " + "**" + str(rolls_list[0]) + "**" + " și " + "**" + str(rolls_list[1]) + "**" + "!")
    except Exception as e:
        print(e)
        await ctx.send("Comandă invalidă!")


async def membrii(ctx):
    index=0
    for m in ctx.guild.members:
        if not m.bot:
            index+=1
    index1=0
    for m in ctx.guild.members:
        if m.bot:
            index1+=1
    await ctx.send("În momentul de față se află " + "**" + str(index) + "**" + " de membrii și " + "**" + str(index1) + "**" + " boți pe serverul " + "**" + str(ctx.message.guild.name) + "**" + "!")


async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("Am intrat pe canal!")
    else:
        await ctx.send("Nu ești într-un canal audio!")


async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Am părăsit canalul!")
        conectat=False
    else:
        await ctx.send("Nu sunt într-un canal audio!")