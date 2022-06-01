"""  Added:
01_Get_Budget_v4,
02_valid_budget_trial2,
03_product_specs_v3,
and 04_unit_separator_v3.

However the quantities collected by 04_unit_separator_v3 haven't been added to
a list. This will be done in the next component as I will need to convert
ml and kg into g and l for easier comparison in the future.
-----
Added:
05_convert_mLKg_v2,
and 06_calculations_v2.

Collapsed functions because they take up too much space/looks like too much
clutter and makes it hard to see the rest of the code.
-----
Added:
Another section from 05_convert_mLKg_v2, which had been added in later on
when I realized it was needed for component 7.
Adjusted the things added from 06_calculations_v2 to 06_calculations_v3.
"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question)  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


def valid_budget(budget_tester):  # makes sure budget is within min and max
    response = budget_tester  # using the previous input from the user
    while True:
        try:  # using try in case it doesnt work
            response = float(response)  # converts into a float if a number
            if 0 < response <= 500:  # Makes sure num is between min and max
                return response   # program continues
            else:
                print("Sorry, this number is not valid")  # error message for
                # a number that is not valid
                response = not_blank("What is your budget?: $")  # re-asks user
        except ValueError:  # if program doesn't work print an error
            print("Sorry you must input a number")  # error message for an
            # input which is not a number
            response = not_blank("What is your budget?: $")  # re-asks user


def num_check(input, question):  # makes sure input is within min and max
    response = input  # using the previous input from the user
    while True:
        try:  # using try in case it doesnt work
            response = float(response)  # converts into a float if a number
            if 0 < response <= 500:  # Makes sure num is between min and max
                return response   # program continues
            else:
                print("Sorry, this number is not valid")  # error message for
                # a number that is not valid
                response = not_blank(question)  # re-asks user
        except ValueError:  # if program doesn't work print an error
            print("Sorry you must input a number")  # error message for an
            # input which is not a number
            response = not_blank(question)  # re-asks user


def unit_error(product_units, user_input):  # function to test for a valid unit
    unit_extractor = "".join((ch if ch in "mliterkogams" else " ") for ch
                              in user_input)  # extracting letters that make
    # up the possible inputs in product_units e.g. "kilos" or "litre"
    units = unit_extractor.replace(" ", "")  # removing spaces
    for list_item in product_units:
        if units in list_item:  # if the input is valid (in product units)
            units = list_item[0]
            return units
    print("Sorry, we are only able to calculate 'g', 'mg', 'l', "
          "and 'ml'")  # error message if not in product units
    return "false"  # Return the message if the input is invalid


def amount_error(user_input):  # function to test for a valid amount
    num_extractor = ''.join((ch if ch in '0123456789.-' else ' ') for ch in
                                user_input)  # extracting numbers 0123456789.
    number = num_extractor.replace(" ", "")  # removes spaces
    try:
        number = float(number)  # convert to float if possible
        if 10000 > number > 0:  # check if number is between min and max
            return number
        else:  # if number outside min and max:
            print("Sorry, that quantity isn't valid. "  
                  "(min = 0, max = 10000)")  # prints error message
            return "false"  # Return the message if the input is invalid
    except ValueError:  # if not a number:
        print("Sorry you must enter a number and unit for the quantity.")
        return "false"  # Return the message if the input is invalid


def calc_average(amounts):  # function that calculates the average unit price
    sum_num = 0
    for t in amounts:
        sum_num = sum_num + t
    avg = f"{sum_num / len(amounts):,.2f}"  # round to 2 dp
    return avg  # returns average


def unit_value(amounts, prices):  # calculates unit prices
    unit_price_list = []  # list to store unit prices
    place = 0
    while place != len(amounts):  # loop until end of list
        amount_item = amounts[place]
        price_item = prices[place]
        unit_price = f"{price_item / amount_item:,.2f}"  # price/amount
        unit_price_list.append(float(unit_price))
        place += 1
    return unit_price_list  # returns the list


# ***** Main routine *****
# --- Brands ---
product_brand = ""
product_brands_list = []  # lists to hold information
brand_number = 1
# --- Price ---
price = ""
price_list = []
# --- Units ---
unit = ""
products_units = [["g", "grams", "gm"], ["kg", "kilo", "kilos", "kilograms"],
                  ["l", "liter", "liters", "litre", "litres"],
                  ["ml", "milliliter", "millilitre"]]  # list of possible units
kg = 1000  # conversion rates
ml = 0.001
amount = ""
amount_list = []  # list to store converted rates
valid = 0  # for unit and amount collector
g_or_l = ""  # finding if they use grams or liters

budget_testers = not_blank("What is your budget?: $")  # Calls function
budget = valid_budget(budget_testers)  # calls function to check valid input
product_type = not_blank("What is the name of the product that you wish to "
                         "compare?: ").title()  # type of product
while product_brand != "X":
    product_brand = not_blank(f"Please enter brand (number {brand_number}), "
                              f"or press <x> to end loop: ").title()  # Get
    # the name of the product
    if product_brand == "X":  # Make sure user user doesn't want to exit
        break
    else:
        brand_number += 1  # to count the number of brands and can be used when
        # extracting information from a list.
        product_brands_list.append(product_brand)  # add product to list
        while valid != 1:  # loop the code until a valid input has been entered
            value_input = input("Please enter the quantity (Use units e.g. 'ml' "
                                "or 'g'): ").lower()
            unit = unit_error(products_units, value_input)
            if unit != "false":  # if either doesn't return false, continue the
                # program
                amount = amount_error(value_input)
            if amount != "false":
                valid += 1

            if unit == "kg":  # if kg, convert to g
                amount = amount*1000
            elif unit == "ml":  # if mL, convert to L
                amount = amount*0.001
            amount_list.append(amount)  # add to list

        if unit == "kg" or "g":
            g_or_l = "g"
        elif unit == "ml" or "l":
            g_or_l = "l"
        price = not_blank("What is the price?: $")  # ask for price and call
        # not_blank()
        price = num_check(price, "What is the price?: $")  # check if integer
        # and convert to float
        price_list.append(price)  # if valid, add to list

unit_value_list = unit_value(amount_list, price_list)  # a list of unit prices
cheapest_item = min(unit_value_list)  # gets most expensive item in list
cheapest_location = unit_value_list.index(cheapest_item)  # finds location of
# cheapest unit value to find the brand associated with it
cheapest_brand = product_brands_list[cheapest_location]  # finding the brand of cheapest
expensive = max(unit_value_list)  # gets most expensive item in list
expensive_location = unit_value_list.index(expensive)  # finds location of most
# expensive item in the list
expensive_brand = product_brands_list[expensive_location]
average_unit_price = calc_average(unit_value_list)  # finds the average unit
# price

