##ServerManager Beta

#imports
from random import randint
import asyncio
import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix = '<')


#variables

#code

##########On ready##############################
print('starting up...')

@bot.event
async def on_ready():
    bot_servers = bot.guilds
    server_num=[x.name for x in bot_servers]
    await bot.change_presence(status =discord.Status.idle , activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(server_num))+' servers, use: <help for help | I am always unstable'))
    print('started!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run('token')