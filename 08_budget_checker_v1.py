"""
----- V1:
This component will check if the cheapest item exceeds the user's budget or
not and recommend which item they should buy.
"""


# ***** Main routine *****
budget = 5.5  # this will not be a set value in the main component
product_brands_list = ["Coke", "Sprite", "L&P", "Fanta"]
price_list = [3, 5, 7, 4]
amount_list = [2, 3, 1, 4]  # list to store converted rates. these will be set
# for testing purposes only.
unit_value_list = [1.5, 1.33, 7.0, 0.25]  # testing only
g_or_l = "g"  # I will have to add this into 05_convert_mLKg_v2.py
cheapest_brand = "Fanta"  # THESE ARE JUST FOR TESTING THEY WILL BE EMPTY
expensive_brand = "L&P"
average_unit_price = 2.52
cheapest_location = 3
expensive_location = 2
# ^ These change in a different component. Will be blank ^

ordered_price_list = unit_value_list
print(unit_value_list)
ordered_price_list.sort()
print(ordered_price_list)
count = 0
while count != len(ordered_price_list):
    locate_number = ordered_price_list[count]
    print(locate_number)
    location = unit_value_list.index(locate_number)
    print(unit_value_list)
    location = unit_value_list.index(0.25)
    print(location)
    test_price = price_list[location]
    if budget > test_price:
        print(test_price)
        print(f"With a budget of ${budget}, we recommend the brand: "
              f"*{product_brands_list[location]}*\nThis is because it is the "
              f"cheapest option whilst still being within your budget.")
        break
    elif budget == test_price:
        print(f"With a budget of ${budget}, we recommend the brand: "
              f"*{product_brands_list[location]}*\nThis is because it is the "
              f"cheapest option whilst still being within your budget."
              f" \n!!ALTHOUGH!!, this is is the limit of your budget!")
        print(test_price)
        break
    elif budget < ordered_price_list[count]:
        count += 1


