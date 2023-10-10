################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """

def getDataPoint(quote):
    bid_price = float(quote['b'])
    ask_price = float(quote['a'])
    price = (bid_price + ask_price) / 2  # Calculate the stock price using the formula
    return {'time': quote['t'], 'price': price, 'size': quote['s']}

def getRatio(data_point_a, data_point_b):
    price_a = data_point_a['price']
    price_b = data_point_b['price']
    
    # Ensure that price_b is not zero to avoid division by zero
    if price_b != 0:
        ratio = price_a / price_b
    else:
        # Handle the case where price_b is zero to avoid division by zero error
        ratio = None  # You can choose an appropriate value or behavior for this case
    
    return ratio


def main():
    # Initialize a dictionary to store stock prices
    prices = {}

    # Your code for setting up the WebSocket connection and subscribing to data goes here

    while True:
        # Receive data from the WebSocket connection
        quote = receiveData()
        
        # Process the received data and get the data point
        data_point = getDataPoint(quote)

        # Store the data point in the prices dictionary using the stock name as the key
        stock_name = quote['symbol']
        prices[stock_name] = data_point['price']

        # Check if you have data for both stock_a and stock_b
        if 'stock_a' in prices and 'stock_b' in prices:
            # Calculate and print the ratio using the getRatio method
            ratio = getRatio(prices['stock_a'], prices['stock_b'])
            print(f"The ratio of stock_a to stock_b is: {ratio}")

if __name__ == '__main__':
    main()





#   stock = quote['stock']
#   bid_price = float(quote['top_bid']['price'])
#   ask_price = float(quote['top_ask']['price'])
#   price = bid_price
#   return stock, bid_price, ask_price, price

# def getRatio(price_a, price_b):
#    """ Get ratio of price_a and price_b """
#    """ ------------- Update this function ------------- """
#    return 1


# Main
# if __name__ == "__main__":
    # Query the price once every N seconds.
#    for _ in iter(range(N)):
#        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

#       """ ----------- Update to get the ratio --------------- """
#        for quote in quotes:
#            stock, bid_price, ask_price, price = getDataPoint(quote)
#            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

#        print("Ratio %s" % getRatio(price, price))
