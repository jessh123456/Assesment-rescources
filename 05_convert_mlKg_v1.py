""" First rundown.
This is just minor component designed to be added into 04_unit_separator_v3.
"""

# ***** Main routine *****
# --- Units ---
unit = "l"  # this input is just for testing purposes - will be blank
kg = 1000  # conversion rates
ml = 0.001
amount = 2  # these values are just for testing purposes
amount_list = []  # list to store converted rates

if unit == "kg":  # if kg, convert to g
    amount = amount*1000
    amount = str(amount) + "g"
elif unit == "ml":  # if mL, convert to L
    amount = amount*0.001
    amount = str(amount) + "L"
elif unit == "g":
    amount = str(amount) + "g"
elif unit == "l":
    amount = str(amount) + "L"
amount_list.append(amount)  # add to list
print(amount_list)  # for testing purposes


