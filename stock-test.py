# test py file for robin stocks

# imports
import os
import datetime
import robin_stocks as rs

# user info 
robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

# main 
def main(stock): 
# login to robinhood
   rs.login(username=robin_user, 
           password=robin_pass, 
           expiresIn=86400, 
           by_sms=True)

   now = datetime.datetime.now()
   print("******************")  
   print("DATE: " + now.strftime('%m-%d-%Y'))     
   print("TIME: " + now.strftime('%H:%M:%S'))
   print("******************")

   stock_price=str(rs.stocks.get_latest_price((stock), priceType=None, includeExtendedHours=True))
   print(stock + ": " + "$" + stock_price[2:stock_price_len-6])


# main runner
if __name__ == "__main__":
    main()
