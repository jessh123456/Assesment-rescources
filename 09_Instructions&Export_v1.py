""" Printing instructions
----- V1:
Borrowing not_blank() function

"""


def not_blank(question):  # checks to make sure input is not blank
    while True:
        response = input(question)  # Gets input from user
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response  # returns response / project continues


def print_instructions(yes_no):
    choice = ""
    while not choice:
        choice = not_blank("Would you like to read the instructions?: "
                           "").lower()
        choice = (get_yes_no(choice, yes_no))
    if choice == "Y":
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
              "Unfortunately we are unable to calculate American/any other \n"
              "foreign units - European only.\n\n"
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

    print("Program launches...")


def get_yes_no(choice, yes_no_valid):
    error = "Sorry that's not a valid choice, try saying 'yes' or 'no'\n"
    for list_item in yes_no_valid:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(error)


# ***** Main routine *****
yes_no = [["y", "yes"], ["n", "no"]]
print("***********************************************************")
print("      **** Welcome to the Price Comparer program ****\n")
print_instructions(yes_no)
