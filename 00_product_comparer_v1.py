"""  Added:
01_Get_Budget_v4,
02_valid_budget_trial2,
03_product_specs_v3,
and 04_unit_separator_v3.

However the quantities collected by 04_unit_separator_v3 haven't been added to
a list. This will be done in the next component as I will need to convert
ml and kg into g and l for easier comparison in the future.
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
amount = ""
valid = 0  # for unit and amount collector

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
        price = not_blank("What is the price?: ")  # ask for price and call
        # not_blank()
        price = num_check(price, "What is the price?: $")  # check if integer
        # and convert to float
        price_list.append(price)  # if valid, add to list
print(product_type, product_brands_list, price_list)

