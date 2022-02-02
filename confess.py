import discord
from discord.ext import commands
import random_name_generator as rng

client = commands.Bot(command_prefix='!', help_command=None)
outputID = 885406314749112351 #venting channel, or output
responseID = 933850247979995136 #venting-response, not currently used.
cookie = 418160770321350667 #our lord and savior

words = ["want to die", "kill myself", "hate myself", "suicide", "not exist", "dont matter", "don't matter", "don't want to be alive", "dont want to be alive", "cutting", "noose", "gun", "revolver"] #words that trigger suicide response
spam_words = ["add ur own words"] # anti-spam shit cuz apparently i need that

support = "If you are about to commit suicide, please don't. Suicide is not painless. It will hurt. Alot.\nIt is a permanent solution to a temporary problem. \n\nSuicide Hotline: +1-800-273-8255\nImpartial Facts about Suicide: lostallhope.com\nSuicide Chatting Hotline: iamalive.org, crisistextline.org" #suicide message
dumbass = "One of the words in your message contains words that may be off topic. If this is a mistake, please message the bot with the tag ->sus at the start of your message, and cookie will manualy send the message. The message will be completely anonomous." #anti-spam filter message

@client.event
@commands.dm_only()
async def on_message(message):
    user = message.author
    name = rng.generate_one() + ": "
    msg = message.content

    if msg.lower().startswith("HIDDEN COMMAND"): #announcement command, hidden so u guys cant impersonate me
        name = "**ANNOUNCEMENT**: "
        msg = msg.replace("HIDDEN COMMAND ", "", 1)

    output = client.get_channel(outputID)

    if message.author == client.user:
        return   


    if isinstance(message.channel, discord.channel.DMChannel):
        skip = False
        dumdum = False
        sad = False
        for i in words: 
            if i in msg.lower() and user.id != cookie: #suicide trigger
               sad = True

        for i in spam_words:
            if i in msg.lower() and user.id != cookie: #anti-spam trigger
                dumdum = True
                skip = True

        if msg.lower().startswith("->sus"): #message sent to me for review
            skip = True
            sad = False
            dumdum = False
            await client.get_user(cookie).send(msg)
            

        if skip == False: # sending msg check 
            await output.send(name + msg) # send message
            if message.attachments != []: # attachment check
                for i in message.attachments: # send all atachments
                    await output.send(i.url)

        if dumdum == True: # anti-spam message
            await user.send(dumbass)

        if sad == True: # suicide message
            await user.send(support) 
            


    if message.channel.id == outputID: # no messages in venting
        await message.delete()
        await user.send("Please do not send messages into venting. If you are attempting to vent, please message me instead. If responding to a vent, please send it into venting-response. This is for anti-off-topic reasons. Your message was: " + msg)

@client.event
async def on_ready(): #check if bot runs or not
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name="DM me, and i'll send a message to venting anonymously", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

client.run('KEY')
