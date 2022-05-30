""" Based on 06_calculations_v1.py
----- V1:
Is able to calculate the average unit price, cheapest item, and most expensive
item. In the next version I will connect them to their brands.
Borrowed the 'calc_average()' function from:
https://www.guru99.com/find-average-list-python.html
and re-arranged the code to fit my own.
----- V2:
Including brand list to relate the cheapest and most expensive items back to
their actual brand.
"""


def calc_average(amounts):  # function that calculates the average unit price
    sum_num = 0
    for t in amounts:
        sum_num = sum_num + t
    avg = sum_num / len(amounts)
    return avg  # returns average


def unit_value(amounts, prices):  # calculates unit prices
    unit_price_list = []  # list to store unit prices
    place = 0
    while place != len(amounts):  # loop until end of list
        amount_item = amounts[place]
        price_item = prices[place]
        unit_price = price_item/amount_item  # divides price by amount
        unit_price_list.append(unit_price)
        place += 1
    return unit_price_list  # returns the list


# ***** Main routine *****
# --- Units ---
brand_list = ["Coke", "Sprite", "L&P", "Fanta"]
price_list = [3, 4, 7, 1]
amount_list = [2, 3, 1, 4]  # list to store converted rates. these will be set
# for testing purposes only.
unit_value_list = unit_value(amount_list, price_list)  # a list of unit prices
cheapest_item = min(unit_value_list)  # gets most expensive item in list
cheapest_location = unit_value_list.index(cheapest_item)  # finds location of
# cheapest unit value to find the brand associated with it
cheapest_brand = brand_list[cheapest_location]  # finding the brand of cheapest
expensive = max(unit_value_list)  # gets most expensive item in list
expensive_location = unit_value_list.index(expensive)  # finds location of most
# expensive item in the list
expensive_brand = brand_list[expensive_location]
average_unit_price = calc_average(unit_value_list)  # finds the average unit
# price
print(unit_value_list)
print(cheapest_brand)
print(expensive_brand)
print(average_unit_price)
# ^ testing purposes only ^



