""" First rundown.
This is just minor component designed to be added into 04_unit_separator_v3.
----- V2:
I realized that i shouldn't add "g" and "L" onto the end because I will need
the values separated when calculating the cheapest and most expensive option
in the future. I have also made kg and ml constants.
"""

# ***** Main routine *****
# --- Units ---
unit = ""  # this input is just for testing purposes - will be blank
KG = 1000  # conversion rates - CONSTANTS
ML = 0.001
amount = 0  # these values are just for testing purposes
amount_list = []  # list to store converted rates

# Below was stuff added later on. this is going to be used for component 7.
g_or_l = ""  # finding if they use grams or liters

if unit == "kg" or "g":
    g_or_l = "g"
elif unit == "ml" or "l":
    g_or_l = "l"

if unit == "kg":  # if kg, convert to g
    amount = amount*KG
elif unit == "ml":  # if mL, convert to L
    amount = amount*ML

amount_list.append(amount)  # add to list
print(amount_list)  # for testing purposes




