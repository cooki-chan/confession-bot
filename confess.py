import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', help_command=None)
outputID = 885406314749112351 #This is channel id, change this to whatever channel you want this to be

@client.event
@commands.dm_only()
async def on_message(message):
    user = message.author
    output = client.get_channel(outputID)

    if message.author == client.user:
        return   
    if isinstance(message.channel, discord.channel.DMChannel):
        await output.send(message.content)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run('BOT-KEY') #Change this key to your own bot
