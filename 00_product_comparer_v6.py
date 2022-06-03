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
-----
Added:
07_print_table,
and 08_budget_checker_v2.
-----
I decided that I wanted to swap the question 'what is your budget' and the
one asking for the name of the product around. I chose this because the user
might be confused why the program is asking for a budget - e.g what is the
budget for?
-----
Added 09_Instructions&Export_v2 then changed it and added
09_Instructions&Export_v3. Also added
recommended = product_brands_list[location]  # FOR COMPONENT 9
to export recommended item.
-----
Fixing changing things as requested by my end user testing.
- Making the quantity repeat if there is an error (should have been working,
  but for some reason it wasn't..)


"""

import pandas


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
                return response  # program continues
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
                return response  # program continues
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
        sum_num = sum_num + float(t)
    avg = f"{sum_num / len(amounts):,.2f}"  # round to 2 dp
    return avg  # returns average


def unit_value(amounts, prices):  # calculates unit prices
    unit_price_list = []  # list to store unit prices
    place = 0
    while place != len(amounts):  # loop until end of list
        amount_item = amounts[place]
        price_item = prices[place]
        unit_price = f"{price_item / amount_item:,.3f}"  # price/amount
        unit_price_list.append(unit_price)
        place += 1
    return unit_price_list  # returns the list


def add_dollar_sign(list_type):  # adds a dollar sign to each item in the list
    # to make it aesthetically pleasing.
    loop = 0
    converted_list = []
    while loop != len(price_list):
        converted_list.append('$' + str(list_type[loop]))  # adds dollar sign
        loop += 1
    return converted_list  # return values with dollar sign added


def print_instructions(yes_no):  # Function to call the instructions
    choice = ""
    while not choice:  # repeat until a valid input is entered
        choice = not_blank("Would you like to read the instructions?: "
                           "").lower()
        choice = (get_yes_no(choice, yes_no))  # calls function
    if choice == "Y":  # if user enters yes
        print("\n***********************************************************\n"
              "\n\t\t**** Product Comparer INSTRUCTIONS ****\n"
              "\nYou will be asked to input the name of the product you wish\n"
              "to compare. NOTE: this is not the brand names, rather the \n"
              "topic of the items. e.g. milk, bread.\n\n"
              "The program will then ask for your budget. This is so you \n"
              "don't overspend even if the other option is cheaper in unit \n"
              "price. This is because the program is designed to save money\n"
              "- not make the user spend more. \n"
              "The following questions will then be repeated until you exit\n"
              "(Press 'x' to exit)\n\n"
              "\t- Please enter brand (number 1), or press <x> to end loop:\n"
              "Enter the name of the brand so that you can identify which \n"
              "item is which. (the number will increase so you know how many\n"
              "items you have entered)\n\n"
              "\t- Please enter the quantity (Use units e.g. 'ml or 'g': \n"
              "Enter a quantity WITH units attached, e.g. 250g, or 0.3L.\n"
              "Unfortunately we are unable to calculate Imperial/any other \n"
              "foreign units - Metric only.\n\n"
              "\t - What is the price?: $\n"
              "Please don't add your own $ sign in front of your price. This\n"
              "has already been done for you. We can only calculate $\n"
              "currency.\n\n"
              "These questions will continue until you press x on the FIRST \n"
              "question. \n"
              "Once you press <x>, the program will display all your \n"
              "information in a table layout. It will also tell you which \n"
              "option we recommend to you. This finds the cheapest unit \n"
              "price whilst still keeping the total price below your budget.\n"
              "You will also be displayed with the cheapest, most expensive,\n"
              "and average unit prices. \n"
              "\nAll this information is also outputted to a .csv file,\n"
              "which can be located in the same directory where the program\n"
              "is stored."
              "\n**********************************************************\n")


# Prints Instructions


def get_yes_no(choice, yes_no_valid):  # see if user says yes or no
    error = "Sorry that's not a valid choice, try saying 'yes' or 'no'\n"
    # error message
    for list_item in yes_no_valid:
        if choice in list_item:
            choice = list_item[0].title()
            return choice  # returns user's input
    print(error)


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
KG = 1000  # conversion rates
ML = 0.001
amount = ""
amount_list = []  # list to store converted rates
valid = 0  # for unit and amount collector
g_or_l = ""  # finding if they use grams or liters

cheapest_brand = ""  # THESE ARE JUST FOR TESTING THEY WILL BE EMPTY
expensive_brand = ""
average_unit_price = 0
cheapest_location = 0
expensive_location = 0

yes_no = [["y", "yes"], ["n", "no"]]  # valid inputs for instructions
recommended = ""

# Welcome message
print("***********************************************************")
print("      **** Welcome to the Price Comparer program ****\n")
print_instructions(yes_no)

product_type = not_blank("What is the name of the product that you wish to "
                         "compare?: ").title()  # type of product
budget_testers = not_blank("What is your budget?: $")  # Calls function
budget = valid_budget(budget_testers)  # calls function to check valid input
while product_brand != "X":
    product_brand = not_blank(f"Please enter brand name {brand_number}, or "
                              f"press <x> to end loop: ").title()  # Get
    # the name of the product
    if product_brand != "X":  # Make sure user user doesn't want to exit
        brand_number += 1  # to count the number of brands and can be used when
        # extracting information from a list.
        product_brands_list.append(product_brand)  # add product to list
        while valid != 1:  # loop the code until a valid input has been entered
            value_input = input(
                "Please enter the quantity (Use units e.g. 'ml' "
                "or 'g'): ").lower()
            unit = unit_error(products_units, value_input)
            amount = amount_error(value_input)
            if unit != "false" and amount != "false":  # if either doesn't
                # return false, continue the
                # program
                valid += 1
        valid = 0  # re-sets for quantity

        if unit == "kg":  # if kg, convert to g
            amount = amount * KG
        elif unit == "ml":  # if mL, convert to L
            amount = amount * ML
        amount_list.append(amount)  # add to list

        if unit == "kg" or unit == "g":
            g_or_l = "g"
        elif unit == "ml" or unit == "l":
            g_or_l = "l"

        price = not_blank("What is the price?: $")  # ask for price and call
        # not_blank()
        price = num_check(price, "What is the price?: $")  # check if integer
        # and convert to float
        price_list.append(price)  # if valid, add to list
    if not product_brands_list:
        print("Sorry you must enter at least one brand!")
        product_brand = ""

unit_value_list = unit_value(amount_list, price_list)  # a list of unit prices
cheapest_item = min(unit_value_list)  # gets most expensive item in list
cheapest_location = unit_value_list.index(cheapest_item)  # finds location of
# cheapest unit value to find the brand associated with it
cheapest_brand = product_brands_list[
    cheapest_location]  # finding the brand of cheapest
expensive = max(unit_value_list)  # gets most expensive item in list
expensive_location = unit_value_list.index(expensive)  # finds location of most
# expensive item in the list
expensive_brand = product_brands_list[expensive_location]
average_unit_price = calc_average(unit_value_list)  # finds the average unit
# price

converted_prices = add_dollar_sign(price_list)  # adds dollar sign to each item
converted_unit_price = add_dollar_sign(unit_value_list)

dictionary = {
    "Brand:": product_brands_list,
    "Price:": converted_prices,
    f"Quantity ({g_or_l}):": amount_list,
    "Unit price:": converted_unit_price
}  # Holds all the information for the dataframe

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

ordered_price_list = unit_value_list.copy()  # copies unit_value_list()
ordered_price_list.sort()  # order the list in ascending order
count = 0  # loops code and locates position of item
while count != len(ordered_price_list):  # loop through all prices
    locate_number = ordered_price_list[count]  # locate the cheapest item
    location = unit_value_list.index(locate_number)  # find item position
    test_price = price_list[location]  # find where it is in price_list
    if budget > test_price:  # if less than budget
        print(f"With a budget of ${budget}, we recommend the brand: "
              f"*{product_brands_list[location]}* for {product_type} brands."
              f"\nThis is because it is the "
              f"cheapest option whilst still being within your budget.")
        recommended = product_brands_list[location]  # FOR COMPONENT 9
        break
    elif budget == test_price:  # if equal to budget
        print(f"With a budget of ${budget}, we recommend the brand: "
              f"*{product_brands_list[location]}* for {product_type} brands."
              f"\nThis is because it is the "
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

# converting variables into lists for the exported frame.
cheapest_brand = [cheapest_brand]
expensive_brand = [expensive_brand]

average_unit_price = ["$" + average_unit_price]

if not recommended:
    recommended = ["None"]
else:
    recommended = [recommended]
# Makes data frame to export
export_frame = pandas.DataFrame([converted_prices, amount_list,
                                 converted_unit_price, cheapest_brand,
                                 expensive_brand, average_unit_price,
                                 recommended],
                                index=['Price:', f'Quantity({g_or_l}):',
                                       'Unit Price', 'Cheapest Brand:',
                                       'Expensive Brand:',
                                       'Average Unit Price:', "Recommended"],
                                columns=[product_brands_list])
# NOTE! I WILL USE THE CONVERTED PRICES WITH DOLLAR SIGNS FOR BETTER APPEARANCE
# IN THE ACTUAL THING
# Exports dataframe to excel file
export_frame.to_csv("Product Information.csv")
# Prints reminder to user their information has been exported
print("-------------------------------------------------------------------")
print("Data has now been exported to the excel file 'Product Information'.")
