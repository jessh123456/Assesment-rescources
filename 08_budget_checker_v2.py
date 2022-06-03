"""
----- V1:
This component will check if the cheapest item exceeds the user's budget or
not and recommend which item they should buy.
----- V2:
Wondered why it would print the wrong brand. This was because I changed
the order of the unit_value_list. Now I will use the .copy() method to fix this
 issue
ADDED recommended = product_brands_list[location] TO BE EXPORTED IN COMPONENT 9
"""


# ***** Main routine *****
budget = 4  # this will not be a set value in the main component
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

ordered_price_list = unit_value_list.copy()  # copies unit_value_list()
ordered_price_list.sort()  # order the list in ascending order
count = 0  # loops code and locates position of item
while count != len(ordered_price_list):  # loop through all prices
    locate_number = ordered_price_list[count]  # locate the cheapest item
    location = unit_value_list.index(locate_number)  # find item position
    test_price = price_list[location] # find where it is in price_list
    if budget > test_price:  # if less than budget
        print(f"With a budget of ${budget}, we recommend the brand: "
              f"*{product_brands_list[location]}*\nThis is because it is the "
              f"cheapest option whilst still being within your budget.")
        recommended = product_brands_list[location]  # FOR COMPONENT 9
        break
    elif budget == test_price:  # if equal to budget
        print(f"With a budget of ${budget}, we recommend the brand: "
              f"*{product_brands_list[location]}*\nThis is because it is the "
              f"cheapest option whilst still being within your budget."
              f" \n!!ALTHOUGH!!, this is the limit of your budget!")
        recommended = product_brands_list[location]  # FOR COMPONENT 9
        break
    elif budget < test_price:  # if more than budget
        count += 1  # loop the code
if count == len(ordered_price_list):
    print(f"With a budget of ${budget}, we are unable to recommend any brands."
          f" \nThis is because the price of the products exceed your desired "
          f"budget.")  # Error message if there is no item less than budget
