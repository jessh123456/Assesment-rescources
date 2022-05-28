txt = "250 KG".lower()
newstr = ''.join((ch if ch in 'MLKGmlkg' else ' ') for ch in txt)
newstr.strip(' ')
print(newstr)
if newstr == "Kg":
    print("yes")
listOfNumbers = [i for i in newstr.split()]
print(listOfNumbers)
