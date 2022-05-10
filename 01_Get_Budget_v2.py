"""Based on 01_Get_Budget_v1:
----- V1:
Component asking user for their budget and checking if input hasn't been
left blank
Calling function not_blank so it cant be used in future user inputs
----- V2:
Adding a dollar sign to question so users don't add one themselves and confuse
the program.
Error message now being included as second parameter when calling the function
"""


def not_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)  # Prints error message
        else:
            return response


# ***** Main routine *****
budget = not_blank("What is your budget?: $", "You can't leave this blank...")
