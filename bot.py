# python bot for Discord server 'toxic_' 
# last updated 4/18/2020

# import important packages
import os
import discord
import random
from dotenv import load_dotenv

# load in variables from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('SERVER')

# declare client as our current Discord client running
client = discord.Client()

# test function
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

# returns back info in terminal to user
@client.event
async def on_ready():
    print('Logged in as: ')
    print(client.user.name)
    print(client.user.id)
    print('----------')

# return gimli quotes
@client.event
async def on_message(message):
        if message.author == client.user:
                    return

        random_quotes=[
                            'Speak, or I will put a dint in your hat that even a wizard will find hard to deal with!',
                            'I name you Elf-friend; and may the stars shine upon the end of your road!',
                            'Nobody tosses a dwarf!',
                            'Not the beard!',
                            'Well, here’s one Dwarf she won’t ensnare so easily.',
                            'Henceforth I will call nothing fair unless it be her gift to me.',
                            'HE STANDS NOT ALONE. YOU WOULD DIE BEFORE YOUR STROKE FELL.',
                            'If anyone was to ask for my opinion, which I note they’re not, I’d say we were taking the long way around.',
                            'Let them come. There is one Dwarf yet in Moria who still draws breath.',
                      ] 
        
                            
        if message.content == 'gimli!':
            response = random.choice(random_quotes)
            await message.channel.send(response)

#        if message.content == 'weeb!':
#            random_int = random.randint(1,10)
#            if random_int == 1:
#                response = 'I need someone gentle. Can you help?'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test1.jpg'))
#            if random_int == 2:
#                response = 'I\'ve had such a long day...can I rub your shoulders?'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test2.jpg'))
#            if random_int == 3:
#                response = 'Notice me senpai!'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test3.jpg'))
#            if random_int == 4:
#                response = 'Ughhhh senpai!'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test4.jpg'))
#            if random_int == 5:
#                response = 'What do you want for Christmas? What do you *really* want?'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test5.jpg'))
#            if random_int == 6:
#                response = 'Oh you need a hand with THAT? Well alright...'
#                await message.channel.send(response)
#               await message.channel.send(file=discord.File('pics/test6.jpg'))
#            if random_int == 7:
#                response = 'I hope you don\'t mind that I brought a friend.'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test7.jpg'))
#            if random_int == 8:
#                response = 'Men never crave what they already have.'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test8.jpg'))
#            if random_int == 9:
#                response = 'What\'re you looking at, Curtis?'
#                await message.channel.send(response)                
#                await message.channel.send(file=discord.File('pics/test9.jpg'))
#            if random_int == 10:
#                response = 'Meow...........meow'
#                await message.channel.send(response)
#                await message.channel.send(file=discord.File('pics/test10.jpg'))

client.run(TOKEN)

