""" Adding intoProduct specifications

----- Version 1:
Borrowing not_blank() function from component 2.
Component 4 will ask for units/amount so I will leave a space which I will add
into this code once added to the main base.
----- Version 2:
getting an error stating amount = amount[0] is out of range. trying different
ways to fix this error
----- Version 3:
Error was due to the fact the numbers are being added to a list and therefore
if the list is left empty, then there is an error when trying to find something
that doesn't exist in a list.
"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question).title()  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


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
# --- Units ---
unit = ""
products_units = [["g", "grams", "gm"], ["kg", "kilo", "kilos", "kilograms"],
                  ["l", "liter", "liters", "litre", "litres"],
                  ["ml", "milliliter", "millilitre"]]  # list of possible units
kg = 1000  # will be used in the next component
ml = 0.001
amount = ""
amount_list = []  # to store the quantities in the next component

valid = 0
while valid != 1:  # loop the code until a valid input has been entered
    value_input = input("Please enter the quantity (Use units e.g. 'ml' "
                        "or 'g'): ").lower()
    unit = unit_error(products_units, value_input)
    if unit != "false":  # if either doesn't return false, continue the program
        amount = amount_error(value_input)
    if amount != "false":
        valid += 1
print(unit, amount)  # for testing purposes
