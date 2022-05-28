""" First breakdown
----- Trial 1:
Not testing for a invalid input at the moment, just getting the whole program
to add things to the appropriate lists and perform correctly as required.
NOTE: THIS PROGRAM WAS SCRAPPED HALFWAY BECAUSE A CLEAR SOLUTION WAS NOT
OBVIOUS; THEREFORE HOURS WOULD HAVE BEEN WASTED ON A PROGRAM THAT FAILED TO
WORK.
-----
Realised this program could have worked, however it was too confusing for the
users as there are too many inputs.
"""


def unit_error(product_units):
    valid = ""
    while not valid:
        check_unit = input("units: ").lower()
        if check_unit not in product_units:
            print("Sorry, we are only able to calculate 'g', 'mg', 'l', "
                  "and 'ml'")
            print(product_units)
        elif check_unit in product_units:
            return check_unit


def quantity_checker(amounts):
    valid = ""
    while not valid:
        try:
            float(amounts)
            return amounts
        except ValueError:
            print("Sorry,you must enter a number")


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question)  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


# ***** Main routine *****
# --- Units & Amounts ---
amount_list = []
unit = ""
unit_list = []
products_units = ["g", "kg", "l", "ml"]
kg = 1000
ml = 0.001

amount = not_blank("How much?: ")
amount = quantity_checker(amount)
amount_list.append(amount)
unit = unit_error(products_units)
print(amount_list, unit)

