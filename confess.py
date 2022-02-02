import discord
from discord.ext import commands
import random_name_generator as rng

client = commands.Bot(command_prefix='!', help_command=None)
outputID = 885406314749112351
responseID = 933850247979995136
cookie = 418160770321350667

words = ["want to die", "kill myself", "hate myself", "suicide", "not exist", "dont matter", "don't matter", "don't want to be alive", "dont want to be alive", "cutting", "noose", "gun", "revolver"]
spam_words = ["horny", "cock", "coc", "ass", "clap", "nigga", "nigger", "faggot", "fag", "boner", "penis", "daniel", "ball", "amog", "cum"]

support = "If you are about to commit suicide, please don't. Suicide is not painless. It will hurt. Alot.\nIt is a permanent solution to a temporary problem. \n\nSuicide Hotline: +1-800-273-8255\nImpartial Facts about Suicide: lostallhope.com\nSuicide Chatting Hotline: iamalive.org, crisistextline.org"
dumbass = "One of the words in your message contains words that may be off topic. If this is a mistake, please message the bot with the tag ->sus at the start of your message, and cookie will manualy send the message. The message will be completely anonomous."

@client.event
@commands.dm_only()
async def on_message(message):
    user = message.author
    name = rng.generate_one() + ": "
    msg = message.content

    if msg.lower().startswith("HIDDEN COMMAND"):
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
            if i in msg.lower() and user.id != cookie:
               sad = True

        for i in spam_words:
            if i in msg.lower() and user.id != cookie:
                dumdum = True
                skip = True

        if msg.lower().startswith("->sus"):
            skip = True
            sad = False
            dumdum = False
            await client.get_user(cookie).send(msg)
            

        if skip == False:
            await output.send(name + msg)
            if message.attachments != []:
                for i in message.attachments:
                    await output.send(i.url)

        if dumdum == True:
            await user.send(dumbass)

        if sad == True:
            await user.send(support) 
            


    if message.channel.id == outputID: 
        await message.delete()
        await user.send("Please do not send messages into venting. If you are attempting to vent, please message me instead. If responding to a vent, please send it into venting-response. This is for anti-off-topic reasons. Your message was: " + msg)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name="DM me, and i'll send a message to venting anonymously", type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

client.run('KEY')
