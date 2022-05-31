""" Based on 07_print_table_v2
----- V1:
First breakdown and working out how to get it to work.
----- V2:
In this version I wanted the prices to start with a $ sign, so I added some
code. This will put a dollar sign in front of all the prices and make it more
appealing to the eye/easy to read and therefore user friendly.
----- V3:
Removed name = ["Coke", "Sprite", "L&P", "Fanta"] and used product_brand_list
instead.
Also turns the dollar sign adder into a function as i will need it for unit
prices and prices.
When displaying the cheapest and most expensive brand I have added their unit
price to make it easier for the user.
"""

import pandas


def add_dollar_sign(list_type):  # adds a dollar sign to each item in the list
    # to make it aesthetically pleasing.
    loop = 0
    converted_list = []
    while loop != len(price_list):
        converted_list.append('$' + str(list_type[loop]))  # adds dollar sign
        loop += 1
    return converted_list  # return values with dollar sign added


# ***** Main routine *****
product_brands_list = ["Coke", "Sprite", "L&P", "Fanta"]
price_list = [3, 4, 7, 1]
amount_list = [2, 3, 1, 4]  # list to store converted rates. these will be set
# for testing purposes only.
unit_value_list = [1.5, 1.33, 7.0, 0.25]  # testing only
g_or_l = "g"  # I will have to
cheapest_brand = "Fanta"  # THESE ARE JUST FOR TESTING THEY WILL BE EMPTY
expensive_brand = "L&P"
average_unit_price = 2.52
cheapest_location = 3
expensive_location = 2
# ^ These change in a different component. Will be blank ^

# Stores the prices with the dollar sign added
converted_prices = add_dollar_sign(price_list)
converted_unit_price = add_dollar_sign(unit_value_list)

dictionary = {
    "Brand:": product_brands_list,
    "Price:": converted_prices,
    f"Quantity ({g_or_l}):": amount_list,
    "Unit price:": converted_unit_price
}

product_frame = pandas.DataFrame(dictionary)  # arrange in a table
product_frame = product_frame.set_index("Brand:")  # make index 'Brands: '
print(product_frame)  # print frame
print("***************************************")
print(f"Cheapest brand: *{cheapest_brand}* "
      f"(${unit_value_list[cheapest_location]})")  # displaying cheapest item
print(f"Most expensive brand: *{expensive_brand}* "
      f"(${unit_value_list[expensive_location]})")  # displaying expensive item
print(f"Average unit price: ${average_unit_price}")  # display avg unit price
print("***************************************")

