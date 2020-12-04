# python bot for Discord server 'toxic_' 
# last updated 4/18/2020

# import important packages
import requests
from pyowm import OWM
import re
import os
import discord
import random
import datetime
import robin_stocks as rs
from dotenv import load_dotenv

# load in variables from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('SERVER')

# weather
API_key = "3b35bed55ea3e8d31402bfa9fdd9aef7"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
owm = OWM('3b35bed55ea3e8d31402bfa9fdd9aef7')

# robinhood 
robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

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
        # ignore if self is sender 
        if message.author == client.user:
                    return

        # for gimli quotes
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
        
        # get gimli quote
        if message.content == 'gimli!':
            response = random.choice(random_quotes)
            await message.channel.send(response)

        # meteor for tanner
        if message.content == 'meteors!':
            with open('meteor_pics/taurids.jpg') as f:
                rand_int = random.randint(1,5)
                if rand_int == 1: 
                    await message.channel.send("Active between October 20 and December 10, 2020, the Northern Taurids peak late the night of Wednesday, November 11, 2020, and into the predawn hours of Thursday, November 12, 2020, when the moon will only be 15 percent full. Expect only about five meteors per hour during this shower, so don’t feel much FOMO if you don’t see this one.")
                    await message.channel.send(file=discord.File('meteor_pics/taurids.jpg'))
                elif rand_int == 2:
                    await message.channel.send("Active between December 27, 2020, and January 10, 2021, the Quadrantids peak late at night on Saturday, January 2 and into early Sunday morning in 2021. The moon will be 84 percent full, so if you go out to watch this meteor shower you might have to struggle with too much moonlight in addition to potentially poor weather. Under the best conditions, you’ll see an average of 25 meteors per hour during the Quadrantids, making it one of the stronger showers of the year.")
                    await message.channel.send(file=discord.File('meteor_pics/quadrantid.jpg'))
                elif rand_int == 3:
                    await message.channel.send("In exceptional years, the Orionids can produce up to 75 meteors per hour. But that hasn’t happened since 2009. In a normal year, as 2020 is predicted to be, expect between 10 to 20 meteors per hour. For peak activity, you’ll want to head out in the predawn hours on October 21. The moon is expected to be just 23 percent full that night, but the shower is active between October 2 and November 7, 2020. ")        
                    await message.channel.send(file=discord.File('meteor_pics/orionid.jpg'))
                elif rand_int == 4:
                    await message.channel.send("While the Leonids can produce outbursts of activity in certain years, 2020 is expected to only get about 10 to 15 meteors per hour during the shower’s peak on the night of Monday, November 16, into the predawn hours of November 17, when the moon will only be 5 percent full. Lasting from November 6 to 30, 2020, the Leonids are known for particularly bright meteors.")
                    await message.channel.send(file=discord.File('meteor_pics/leonids.jpg'))
                elif rand_int == 5:
                    await message.channel.send("The Geminids are the strongest meteor shower of the year. And in 2020, the peak falls on the night of Sunday, December 13, when the moon will only be at 1 percent, providing ideal dark sky conditions. In the Northern Hemisphere, you’ll be able to see meteors from about 11 p.m. onward. If you’re in the Southern Hemisphere—perhaps to see the total solar eclipse in Chile and Argentina—you’ll have to stay up into the early morning hours of December 14 to see the show. But it’s worth it—up to 75 meteors per hour are expected during the Geminids each year. The entire shower lasts from December 4 to 17, 2020.")
                    await message.channel.send(file=discord.File('meteor_pics/geminids.jpg'))


        # weather
        if re.search("weather!", message.content):
            x = re.split('weather!', message.content)
            city_name = x[1]
            test_city = owm.weather_at_place(city_name)
            test_weather = test_city.get_weather()
            test_temp = test_weather.get_temperature('fahrenheit')['temp']
            result = "\nCurrent Temperature in" + city_name + ": " + str(test_temp) + "*F"
            # print("\nCurrent Temperature in " + city_name + ": " + str(test_temp) + "*F")
            # Final_url = base_url + "appid=" + API_key + "&q=" + city_name
            # weather_data = requests.get(Final_url).json()
            await message.channel.send(result)

        # get robinhood stock price
        if re.search("hood!", message.content):
            x = re.split('hood!', message.content)
            stock = x[1]
            rs.login(username=robin_user, 
                     password=robin_pass, 
                     expiresIn=86400, 
                     by_sms=True)
            stock_price=str(rs.stocks.get_latest_price((stock), priceType=None, includeExtendedHours=True))
            stock_price_len = len(str(stock_price))
            formatted_price = str(stock + ": " + "$" + stock_price[2:stock_price_len-6])
            #print(formatted_price)
            await message.channel.send("Current Price of" + stock + "\n->" + formatted_price)

client.run(TOKEN)

