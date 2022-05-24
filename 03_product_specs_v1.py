""" Retry of Product specifications
----- Version 1:
Borrowing 

"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question).title()  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


def unit_error(product_units):
    valid = ""
    while not valid:
        check_unit = input("units: ").lower()
        if check_unit not in product_units:
            print("Sorry, we are only able to calculate 'g', 'mg', 'l', "
                  "and 'ml'")
            print(product_units)
        for list_item in product_units:
            if check_unit in list_item:
                check_unit = list_item[0].title()
                return check_unit


# ***** Main routine *****
product_type = ""
# --- Brands ---
product_brand = ""
product_brands_list = []
brand_number = 1
# --- Price ---
price = ""
price_list = []
# --- Units ---
unit = ""
products_units = [["g", "grams", "gm"], ["kg", "kilo", "kilos", "kilograms"],
                  ["l", "liter", "liters", "litre", "litres"],
                  ["ml", "milliliter", "millilitre"]]
kg = 1000
ml = 0.001
amount = ""
amount_list = []

while product_type != "X":
    if product_brand == "X":
        break
    product_type = not_blank("Product type: ")
    if product_type == "X":
        break
    while product_brand != "X":
        product_brand = not_blank(f"brand ({brand_number}): ").title()
        if product_brand == "X":
            break
        else:

            brand_number += 1
            product_brands_list.append(product_brand)
            amount = not_blank("How much?: ")
            amount_list.append(amount)
            price = not_blank("Price: ")
            price_list.append(price)
print(product_brands_list, price_list, amount_list, product_type)
