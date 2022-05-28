""" Adding into Product specifications + based on 04_unit_separator_trial2

----- Version 1:
Borrowing not_blank() function from component 2.
Component 4 will ask for units/amount so I will leave a space which I will add
into this code once added to the main base.
----- Version 2:
getting an error stating amount = amount[0] is out of range. trying different
ways to fix this error
"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question).title()  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


def unit_error(product_units, user_input):
    valid = ""
    while not valid:
        unit_extractor = "".join((ch if ch in "mliterkogams" else " ") for ch
                                 in user_input)  # extracting letters that make
        # up the possible inputs in product_units e.g. "kilos" or "litre"
        units = [i for i in unit_extractor.split()]
        if not units:
            print("Sorry, we are only able to calculate 'g', 'mg', 'l', "
                  "and 'ml'")
            # print(units)
            user_input = input("Please enter the quantity (Use units e.g. 'ml'"
                               " or 'g'): ").lower()
        else:
            for list_item in product_units:
                if units not in list_item:
                    print("Sorry, we are only able to calculate 'g', 'mg', 'l', "
                          "and 'ml'")
                    # print(units)
                    user_input = input("Please enter the quantity (Use units e.g. 'ml'"
                                       " or 'g'): ").lower()
                    print(units)
                else:
                    units = list_item[0]
                    return units
            print(units)


def amount_error(user_input):
    valid = ""
    while not valid:
        num_extractor = ''.join((ch if ch in '0123456789.' else ' ') for ch in
                                user_input)  # extracting numbers 0123456789.
        number = [float(i) for i in num_extractor.split()]  # convert to float
        number = number[0]
        if 10000 > number > 0:
            return number
        else:
            return "false"


# ***** Main routine *****
# --- Units ---
unit = ""
products_units = [["g", "grams", "gm"], ["kg", "kilo", "kilos", "kilograms"],
                  ["l", "liter", "liters", "litre", "litres"],
                  ["ml", "milliliter", "millilitre"]]
kg = 1000
ml = 0.001
amount = ""
amount_list = []

valid = 0
while valid != 1:
    value_input = input("Please enter the quantity (Use units e.g. 'ml' "
                        "or 'g'): ").lower()
    unit = unit_error(products_units, value_input)
    print(unit)
    amount = amount_error(value_input)
    if amount != "false":
        valid += 1
