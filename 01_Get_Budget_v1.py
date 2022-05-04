"""Component asking user for their budget and storing it in a list
Calling function not_blank so it cant be used in future user inputs"""


def not_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank...")
        else:
            return response


# ***** Main routine *****
budget = not_blank("What is your budget?: ")
