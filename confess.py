import discord as discord
from discord.ext import commands
import random
import json
import os
import threading

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', help_command=None, intents=intents)
outputID = -1 #Channel to send messages (Channel ID)
cookie = -1 #Manual Review User (User ID) 
#-1 IS A PLACEHOLDER

words = [] #Suicide Message Trigger (Sends support)
spam_words = [] #Negative Word Filter (Sends dumbass)

support = "If you are about to commit suicide, please don't. Suicide is not painless. It will hurt. Alot.\nIt is a permanent solution to a temporary problem. \n\nSuicide Hotline: +1-800-273-8255\nImpartial Facts about Suicide: lostallhope.com\nSuicide Chatting Hotline: iamalive.org, crisistextline.org"
dumbass = "One of the words in your message contains words that may be off topic. If this is a mistake, please message the bot with the tag ->sus at the start of your message, and cookie will manualy send the message. The message will be completely anonomous."

@client.event
@commands.dm_only()
async def on_message(message):
    user = message.author
    name = ""
    msg = message.content

    output = client.get_channel(outputID)

    if message.author == client.user:
        return   

    if isinstance(message.channel, discord.channel.DMChannel):
        skip = False
        dumdum = False
        sad = False
        
        for i in words: #Suicidal Message Filter
            if i in msg.lower() and user.id != cookie:
               sad = True

        for i in spam_words: #Filtered Word Filter
            if i in msg.lower() and user.id != cookie:
                dumdum = True
                skip = True

        if msg.lower().startswith("->sus"): #Manual Review Trigger
            skip = True
            sad = False
            dumdum = False
            await client.get_user(cookie).send(msg)
            
        if skip == False:
            if msg != ""   :
                embedVar = discord.Embed(title="", description="", color=0x00ff00)
                if msg.lower().startswith("ADD A PREFIX HERE"): #Used for owner messages! Make sure to change!
                    msg = msg.replace("PREFIX HERE TOO!!! ", "", 1)
                    embedVar.add_field(name="**SYSTEM**:", value=msg, inline=False)
                else:
                    if len(msg) < 1024: #If the message is too long to fit in an embed, send as raw text
                        embedVar.add_field(name="Message:", value=msg, inline=False)
                        await output.send(embed=embedVar)
                    else:
                        await output.send(msg)

            if message.attachments != []: #Send Attatchments (Words in images bypasses filters, be careful.) Images can also be much more triggering, so remove this block if you don't want image support
                for i in message.attachments:
                    await output.send(i.url)

        if dumdum == True: #Send dumbass message
            await user.send(dumbass)

        if sad == True: #Send Support message
            await user.send(support) 
            
    if message.channel.id == outputID: #If a message is sent in the channel the bot talks in, delete (Used to keep convos on topic most of the time)
        await message.delete()
        await user.send("Please do not send messages into venting. If you are attempting to vent, please message me instead. If responding to a vent, please send it into venting-response. This is for anti-off-topic reasons. Your message was: " + msg)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name="DM me, and i'll send a message to venting anonymously", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)
client.run('CLIENT KEY')
