""" Retry of Product specifications
----- Version 1:
Borrowing not_blank() function from component 2.
Component 4 will ask for units/amount so I will leave a space which I will add
into this code once added to the main base.
I want to use the 'budget_tester()' which is used in component 2 to check
that the price inputted is valid. Therefore I have changed the name to
'num_check()' so I can use it for both. This is the function I will use for the
base and adjust component 2 to fit these changes.
----- Version 2:
I'm going to make the inputs more user friendly/attractive to the eye.
"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question).title()  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


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


# ***** Main routine *****
# --- Brands ---
product_brand = ""
product_brands_list = []  # lists to hold information
brand_number = 1
# --- Price ---
price = ""
price_list = []


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
        # ------------
        # This is where I will add in component 4 to call a function
        # ------------
        price = not_blank("What is the price?: ")  # get price-call not_blank()
        price = num_check(price, "What is the price?: $")  # check if integer
        # and convert to float
        price_list.append(price)  # if valid, add to list
print(product_type, product_brands_list, price_list)
