
# the program calculates the total stock based on a set of quantites and prices.
menu = ['Calaloo', 'Rice', 'Dumplings', 'Tofu']

#This is the stock quantity for each iteme
stock = {
    'Calaloo': 50,
    'Rice': 100,
    'Dumplings': 75,
    'Tofu': 30
}

#This is the price for each item
price = {
    'Calaloo': 2.50,
    'Rice': 1.50,
    'Dumplings': 1.00,
    'Tofu': 3.00
}

total_stock_worth = 0
#calculates the stock costs
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value



print("Total stock worth: £", total_stock_worth)
# end of code