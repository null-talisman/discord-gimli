# python bot for Discord server 'toxic_' 
# last updated 4/18/2020
# - added top 2/2/21

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

        # for help info
        help_info="""!gimli - Gimli, Son of Gloin, graces you with his presence.\n!meteors - Knowledge is power.\n!weather <city name> - Should get the weather report for that city.\n!hood <stock> - Gets current price from Robinhood.\n!test - fugaz command\n!top <#> - Gets top X daily movers from Robinhood. Default is 20.
        """
        test_help_info=[
            "!gimli - Gimli, Son of Gloin, graces you with his presence.",
            "!meteors - Knowledge is power.",
            "!weather <city name> - Should get the weather report for that city.",
            "!hood <stock> - Gets current price from Robinhood.",
            "!top <#> - Gets top X daily movers from Robinhood. Default is 20."
            "!test - fugaz command"
        ]
        if message.content == '!help':
            #response = random.choice(random_quotes)
            await message.channel.send(help_info)
        #####################################TESTING##############################################
        #if message.content == '!test':
        #    for item in test_help_info:
        #        await message.channel.send(item)
        #########################################################################################

        # get gimli quote
        if message.content == '!gimli':
            response = random.choice(random_quotes)
            await message.channel.send(response)
        
        # meteor for tanner
        if message.content == '!meteors':
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
        if re.search("!weather", message.content):
            x = re.split('!weather', message.content)
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
        if re.search("!hood", message.content):
            x = re.split('!hood', message.content)
            stock = x[1]
            rs.login(username=robin_user, 
                     password=robin_pass, 
                     expiresIn=86400, 
                     by_sms=False)
            stock_price=str(rs.stocks.get_latest_price((stock), priceType=None, includeExtendedHours=True))
            #
            test_shit=str(rs.stocks.get_stock_historicals((stock), interval='hour', bounds='regular'))
            test2=str(rs.get_top_movers)
            #
            stock_price_len = len(str(stock_price))
            formatted_price = str(stock + ": " + "$" + stock_price[2:stock_price_len-6])
            #print(formatted_price)
            await message.channel.send("Current Price of" + stock + "\n->" + formatted_price)
            for item in test_shit.splitlines():
                print(item)
            #print(test_shit)
            #await message.channel.send("****\n" + test_shit)

        if re.search("!top", message.content):
            x = re.split('!top ', message.content)
            cond = False
            if len(x) > 1:
                top = x[1]
                cond = True
            
            rs.login(username=robin_user, 
                    password=robin_pass, 
                    expiresIn=604800, 
                    by_sms=False)

            top_movers = rs.get_top_movers()
            i=1
            info = []
            for fuck in top_movers:
                symbl = fuck.get("symbol")
                price = fuck.get("last_trade_price")
                new_price = str(price[:(len(price)-4)])
                #print(str(i) + ". " + symbl + " " + new_price)
                info.append(str(i) + ". " + symbl + " $" + new_price)
                i+=1

            if cond == True:
                res = "Top " + top + " Movers\n"
                jank = 0
                while jank < int(top):
                    res = res + info[jank]
                    res = res + "\n"
                    #print(info[jank])
                    jank+=1
                #print(res)
                #return
                await message.channel.send(res)
            else:
                res = "Top 20 Movers:\n"
                for line in info:
                    res = res + line
                    res = res + "\n"
                    #print(line)
                await message.channel.send(res)
            #print(info)
            #await message.channel.send(top_movers)

        if re.search("!about", message.content):
            rs.login(username=robin_user, 
                password=robin_pass, 
                expiresIn=604800, 
                by_sms=False)
            str_len = len(re.split("!about", message.content))
            print(str_len)
            if str_len == 1:
                await message.channel.send("Invalid. Dummy.")
            elif str_len == 2:
                info = []
                spl = re.split("!about", message.content)
                x = spl[1]
                x_high = str(rs.get_fundamentals(x, 'high'))
                x_low = str(rs.get_fundamentals(x, 'low'))
                x_avg_vol = str(rs.get_fundamentals(x, 'average_volume_2_weeks'))
                x_desc = rs.get_fundamentals(x, 'description')
                x_sect = rs.get_fundamentals(x, 'sector')
                x_symb = rs.get_fundamentals(x, 'symbol')
                print("High: " + x_high + "\nLow: " + x_low + "\nAverage Volume (2 Wks): " + x_avg_vol)
                #print("Description: " + x_desc + "\nSector: " + x_sect + "\nSymbol: " + x_symb)
                await message.channel.send("Symbol: "+str(x_symb)+"\nSector: "+str(x_sect)+"\nHigh: $"+str(x_high[2:len(x_high)-6])+"\nLow: $"+str(x_low[2:len(x_low)-6])+"\nAvg Vol: "+str(x_avg_vol[2:len(x_avg_vol)-6]))


client.run(TOKEN)

