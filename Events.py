import discord
from discord.ext import commands
from gtts import gTTS
import os
from mutagen.mp3 import MP3
import time
import random as rnd
import Date


async def hello(message):
    await message.channel.send('Salut!')


async def goodbye(message):
    await message.channel.send('Ceaw!')


async def set(message, string_split):
    Date.limba=string_split[1]
    await message.channel.send("Setat pe " + Date.limba + "!")


async def tts(ctx, text, client):
    index=0
    prop=""
    for cuvant in text:
        if index!=0:
            prop+=cuvant+" "
        index=index+1
    if prop=='':
        await ctx.channel.send('Trebuie să scrii un mesaj după comanda **$tts**!')
        return
    global gTTS
    if ctx.author.voice==None:
        await ctx.channel.send('Nu ești într-un canal audio!')
        return
    channel = ctx.author.voice.channel
    vc = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()
    speech = gTTS(text = prop, lang = Date.limba, slow = False)
    speech.save("sound.mp3")
    vc.play(discord.FFmpegPCMAudio("sound.mp3"))
    

async def alege(ctx, string):
    string = string.replace('$alege ', '')   
    nr_virgula = string.count(',')
    if nr_virgula!=0:
        string = string.replace(' ', '')
        list = string.split(',')
        item = rnd.choice(list)
        await ctx.channel.send("Elementul random din listă generat de " + ctx.author.mention + " este " + "**" + item + "**" + "!")
        return
    list = string.split(' ')
    item = rnd.choice(list)
    await ctx.channel.send("Elementul random din listă generat de " + ctx.author.mention + " este " + "**" + item + "**" + "!")


async def help(message):
    embedVar = discord.Embed(title="Comenzi valabile:", color=0x074ccc)
    embedVar.set_thumbnail(url="https://tadpole.cc/wp-content/uploads/help-1.png")
    embedVar.add_field(name="$join", value="Mă alătur canalului audio", inline=False)
    embedVar.add_field(name="$leave", value="Părăsesc canalul audio", inline=False)
    #embedVar.add_field(name="$set <limba>", value="Setează limba folosită pentru TTS", inline=False)
    #embedVar.add_field(name="$tts <mesaj>", value="Recit un mesaj TTS", inline=False)
    embedVar.add_field(name="$coinflip", value="Dau cu banul", inline=False)
    embedVar.add_field(name="$random <număr> <număr2>", value="Generez un număr random între cele doua numere date de utilizator", inline=False)
    embedVar.add_field(name="$zar", value="Dau cu zarurile", inline=False)
    embedVar.add_field(name="$membrii", value="Afișez numărul de membrii și boți de pe server", inline=False)
    embedVar.add_field(name="$alege", value="Aleg un element aleatoriu dintr-o listă dată de utilizator", inline=False)
    await message.channel.send(embed=embedVar)