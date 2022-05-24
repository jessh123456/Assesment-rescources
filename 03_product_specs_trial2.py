""" First breakdown
----- Trial 1:
Not testing for a invalid input at the moment, just getting the whole program
to add things to the appropriate lists and perform correctly as required.
NOTE: THIS PROGRAM WAS SCRAPPED HALFWAY BECAUSE A CLEAR SOLUTION WAS NOT
OBVIOUS; THEREFORE HOURS WOULD HAVE BEEN WASTED ON A PROGRAM THAT FAILED TO
WORK.
----- Trial 2:

"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question)  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


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
amount = ""
amount_list = []
all_amounts = []

while product_type != "X":
    product_type = input("Product type: ").title()
    if product_type == "X":
        break
    else:
        product_type_list.append(product_type)
    while product_brands != "X":
        product_brands = not_blank(f"brand ({brand_number}): ").title()
        if product_brands == "X":
            break
        else:
            brand_number += 1
            product_brands_list.append(product_brands)
            amount = not_blank("How much?: ")
            amount_list.append(amount)
            price = not_blank("Price: ")
            price_list.append(price)
    all_product_brands_list.append(product_brands_list)
    print(all_product_brands_list)
    product_brands_list.clear()
    all_prices.append(price_list)
    price_list.clear()
    print(all_prices)
    all_amounts.append(amount_list)
    amount_list.clear()
    print(all_amounts)
    product_brands = ""
