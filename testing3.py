
list = [1, 2, 3, 4]
new_list = []
valid = 0
while valid != len(list):
    new_list.append('$' + str(list[valid]))
    valid += 1
print(new_list)
