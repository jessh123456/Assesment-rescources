""" First breakdown
----- V1:
Having a boundary of between 0-500. Checking that the input is a number and
between valid boundaries
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
        if response.isdigit():  # checks that the input is a number
            response = float(response)  # converts into a float if a number
            if 0 < response <= 500:  # Makes sure num is between min and max
                return response   # program continues
            else:
                print("Sorry, this number is not valid")  # error message for
                # a number that is not valid
                response = not_blank("What is your budget?: $")  # re-asks user
        else:
            print("Sorry you must input a number")  # error message for an
            # input which is not a number
            response = not_blank("What is your budget?: $")  # re-asks user


# ***** Main routine *****
budget_testers = not_blank("What is your budget?: $")  # Calls function

budget = valid_budget(budget_testers)  # calls function to check valid input
print(budget)  # for testing purposes to make sure the program works
