# Import the API REST client
from polygon import RESTClient
import os


# I need to make it run slow, 5 times every min
# Will make a function that Grabs the Items
# and in the main For Loop, set a sleep for 25 sec
# Doing this b/c I don't want to pay to be able to 
# do more requests per min, should be enough as a POC


#This is for debugging
Debugging = True
########################################## Functions ##########################################

#Function to Grab the list of Tickers From file and return a list
def get_Tickers(TickerList):
    print("Getting Tickers") if (Debugging) else Debugging
    with open(TickerList, 'r') as f:
        a = f.readlines()
        a = [i.replace("\n", "") for i in a] #Removes all new line characters
        
        if(Debugging):
            for I in a:
                print(I)

        return(a)

#
###############################################################################################
#Initialize the client with the custom API Key
client = RESTClient(api_key="tnXrim4PNLjtuVFcyxNDiCfNvbH1T6pB")

print(get_Tickers('TickerList.txt'))

print(client.list_aggs(ticker='AAPL', multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000))