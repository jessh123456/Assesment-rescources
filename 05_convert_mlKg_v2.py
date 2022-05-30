""" First rundown.
This is just minor component designed to be added into 04_unit_separator_v3.
----- V2:
I realized that i shouldn't add "g" and "L" onto the end because I will need
the values separated when calculating the cheapest and most expensive option
in the future.
"""

# ***** Main routine *****
# --- Units ---
unit = ""  # this input is just for testing purposes - will be blank
kg = 1000  # conversion rates
ml = 0.001
amount = 0  # these values are just for testing purposes
amount_list = []  # list to store converted rates

if unit == "kg":  # if kg, convert to g
    amount = amount*1000
elif unit == "ml":  # if mL, convert to L
    amount = amount*0.001

amount_list.append(amount)  # add to list
print(amount_list)  # for testing purposes


