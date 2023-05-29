import discord
import os
from discord.ext import commands
from keep_awake import keep_awake

import giphy_client
from giphy_client.rest import ApiException
import random

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print(f"we have logged in as {client.user}")

@client.command()
async def siesta(ctx):
  await ctx.channel.send(f"Hi! {ctx.author.mention} it's great to see you")

@client.command()
async def whitey(ctx):
  await ctx.channel.send(f'Hey {ctx.author.mention}! Whiteyntyn migo? WAHAHHAHAHAH \n \n	ԅ(≖‿≖ԅ)')

@client.command()
async def sus(ctx):
  await ctx.channel.send(f'That was suspicious! \n \n (ÒДÓױ)')

@client.command()
async def ahh(ctx):
  await ctx.channel.send(f'	༼ つ ◕_◕ ༽つ')


@client.command()
async def helpme(ctx):
  await ctx.channel.send(f'Hey {ctx.author.mention}! please type (.gif "search anything")')

@client.command()
async def gif(ctx,*,q="random"):
    api_key="4mwKht785I6YvXyTSEZVBokaJsz52A1V"
    api_instance = giphy_client.DefaultApi()
    try: 
        
        api_response = api_instance.gifs_search_get(api_key, q, limit=10, rating='r')
        listahan = list(api_response.data)
        giphy = random.choice(listahan)
        emb = discord.Embed(title=q)
        emb.set_image(url = f'https://media.giphy.com/media/{giphy.id}/giphy.gif')
        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

keep_awake()
client.run(os.environ['blessings'])


#           88                                          
#           ""                        ,d                
#                                     88                
# ,adPPYba, 88  ,adPPYba, ,adPPYba, MM88MMM ,adPPYYba,  
# I8[    "" 88 a8P_____88 I8[    ""   88    ""     `Y8  
#  `"Y8ba,  88 8PP"""""""  `"Y8ba,    88    ,adPPPPP88  
# aa    ]8I 88 "8b,   ,aa aa    ]8I   88,   88,    ,88  
# `"YbbdP"' 88  `"Ybbd8"' `"YbbdP"'   "Y888 `"8bbdP"Y8  