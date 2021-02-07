import discord
import sys
from keep_alive import keep_alive
import os
import asyncio
import youtube_dl
from time import sleep

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('alsalam 3alyko'):
        await message.channel.send('w alakom elsalam')

@client.event
async def on_voice_state_update(user, before_state, after_state):
  if before_state.self_mute == True and after_state.self_mute == False or before_state.channel == None and after_state.channel != None:
    try:
      vc = await after_state.channel.connect()
      vc.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source='slamo3alykom.mp3'))
      while vc.is_playing():
        sleep(.1)
      await vc.disconnect()
    except:
      print("tried to run while already running")
  else:
    try:
      vc = await after_state.channel.connect()
      vc.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source='3alykom_el_salam.mp3'))
      while vc.is_playing():
        sleep(.1)
      await vc.disconnect()
    except:
      print("tried to run while already running")

#keep_alive()
client.run('Nzk1MDY5NDAxMDgyMjMyODM1.X_EAFA.3smmqUKamNbKKMdX2TcVdAToioI')