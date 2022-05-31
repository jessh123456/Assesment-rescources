""" Based on 07_print_table_v1
----- V1:
First breakdown and working out how to get it to work.
----- V2:
In this version I wanted the prices to start with a $ sign, so I added some
code. This will put a dollar sign in front of all the prices and make it more
appealing to the eye/easy to read and therefore user friendly.
"""

import pandas

# ***** Main routine *****
product_brands_list = ["Coke", "Sprite", "L&P", "Fanta"]
price_list = [3, 4, 7, 1]
amount_list = [2, 3, 1, 4]  # list to store converted rates. these will be set
# for testing purposes only.
name = ["Coke", "Sprite", "L&P", "Fanta"]
g_or_l = "g"

converted_prices = []  # Stores the prices with the dollar sign added
loop = 0
while loop != len(price_list):
    converted_prices.append('$' + str(price_list[loop]))
    loop += 1
dictionary = {
    "Brand:": name,
    "Price:": converted_prices,
    f"Quantity ({g_or_l}):": amount_list
}
product_frame = pandas.DataFrame(dictionary)
product_frame = product_frame.set_index("Brand:")
print(product_frame)
