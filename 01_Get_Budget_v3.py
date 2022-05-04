"""Based on 01_Get_Budget_v2:
----- V1:
Component asking user for their budget and checking if input hasn't been
left blank
Calling function not_blank so it cant be used in future user inputs
----- V2:
Adding a dollar sign to question so users don't add one themselves and confuse
the program.
Error message now being included as second parameter when calling the function
----- V3:
.isalpha method now included so that spaces wont be accepted. Removing
valid = "" and replacing it with True.
Putting error message back inside the function so it wont have to be added
when the function is called somewhere else.
"""


def not_blank(question, error_message):
    while True:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# ***** Main routine *****
budget = not_blank("What is your budget?: $", "You can't leave this blank...")
