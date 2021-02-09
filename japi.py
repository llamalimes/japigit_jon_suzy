import urllib.request
import json

def getStockData(symbol):
    URL= "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+symbol+"&apikey=CZ8JZVFFTGH71ZNX"
    connection = urllib.request.urlopen(URL)
    responseString = connection.read().decode()
    return responseString

def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def main():
    #Declare symbol
    symbol = None

    #Run loop until quit is entered.
    while symbol != 'QUIT':
        symbol = input("Stock symbol: ").upper()
        #break out of loop if quit is entered
        if symbol == 'QUIT':
            break
        #Print JSON formatted response to screen
        response = getStockData(symbol)
        print(response)
        #Convert the response from JSON to Python dictionary

        #Trim string for conversion
        response = response.replace('\"Global Quote\": {','')
        response = response[:-1]
        #enclose string in brackets
        #response = '['+ response +']'

        #call on json module to convert string to dictionary
        dictionary = json.loads(response)

        #print price
        print("\nThe current price of",symbol,"is:",dictionary["05. price"],'\n')
    print("Stock Quotes retrieved successfully!")

if __name__ == "__main__":
   main()
