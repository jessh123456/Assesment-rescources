""" First rundown.
"""


def calc_average(amounts):
    sum_num = 0
    for t in amounts:
        sum_num = sum_num + t
    avg = sum_num / len(amounts)
    return avg

def unit_cheapest_value(amounts, prices):
    unit_cheapest = 0
    cheapest = min(amount_list)  # finds the cheapest number in a list
    cheapest_location = amount_list.index(cheapest)  # used to find which brand
    # it relates to
    print(f"The cheapest value is {min(amount_list)}")  # prints cheapest value


# ***** Main routine *****
# --- Units ---
price_list = [3, 4, 7, 1]
amount_list = [2, 3, 1, 4]  # list to store converted rates. these will be set for
# testing purposes only.
cheapest_item = unit_cheapest_value(amount_list, price_list)

expensive = max(amount_list)  # gets most expensive item in list
expensive_location = amount_list.index(expensive)  # finds location of most
# expensive item in the list
print(f"The most expensive value is {max(amount_list)}")  # prints most
# expensive value
average = calc_average(amount_list)
print(f"The average price is ")


