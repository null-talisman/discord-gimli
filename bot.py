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

