""" First breakdown
----- V1:
Having a boundary of between 0-500. Checking that the input is a number and
between valid boundaries
"""


def not_blank(question):
    while True:
        response = input(question)
        if not response or response.isspace():  # Checks input is not blank
            print("You can't leave this blank...")  # Prints error message
        else:
            return response


def valid_budget(budget_tester):
    response = budget_tester
    while True:
        if response.isdigit():
            response = float(response)
            if 0 < response <= 500:
                return response
            else:
                print("Sorry, this number is not valid")
                response = not_blank("What is your budget?: $")
        else:
            print("Sorry you must input a number")
            response = not_blank("What is your budget?: $")


# ***** Main routine *****
budget_testers = not_blank("What is your budget?: $")

budget = valid_budget(budget_testers)
print(budget)
