"""
----- V1:
First breakdown and working out how to get it to work.
"""

import pandas

# ***** Main routine *****
product_brands_list = ["Coke", "Sprite", "L&P", "Fanta"]
price_list = [3, 4, 7, 1]
amount_list = [2, 3, 1, 4]  # list to store converted rates. these will be set
# for testing purposes only.
name = ["Coke", "Sprite", "L&P", "Fanta"]
g_or_l = "g"
dictionary = {
    "Brand": name,
    "Price": price_list,
    f"Quantity ({g_or_l})": amount_list
}

product_frame = pandas.DataFrame(dictionary)
product_frame = product_frame.set_index("Brand")
print(product_frame)

