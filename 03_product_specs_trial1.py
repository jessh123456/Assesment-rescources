""" First breakdown
----- Trial 1:
Not testing for a invalid input at the moment, just getting the whole program
to add things to the appropriate lists and perform correctly as required.
NOTE: THIS PROGRAM WAS SCRAPPED HALFWAY BECAUSE A CLEAR SOLUTION WAS NOT
OBVIOUS; THEREFORE HOURS WOULD HAVE BEEN WASTED ON A PROGRAM THAT FAILED TO
WORK.
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


# ***** Main routine *****
product_type = ""
product_type_list = []
# --- Brands ---
product_brands = ""
product_brands_list = []
all_product_brands_list = []
brand_number = 1
# --- Price ---
price = ""
price_list = []
all_prices = []
# --- Units ---
unit = ""
unit_list = []
products_units = ["g", "kg", "l", "ml"]
kg = 1000
ml = 0.001
amount = 0

while product_type != "X":
    product_type = input("Product type: ").title()
    if product_type == "X":
        break
    else:
        product_type_list = product_type_list.append(product_type)
    while product_brands != "X":
        product_brands = input(f"brand ({brand_number}): ").title()
        brand_number += 1
        product_brands_list.append(product_brands)
        unit = unit_error(products_units)
        amount = input(f"How much?: ")
        price = input(f"price: ")
        price_list.append(price)

    all_product_brands_list.append(product_brands_list)
    print(all_product_brands_list)
