txt = "250 ml"
newstr = ''.join((ch if ch in '0123456789.' else ' ') for ch in txt)
listOfNumbers = [float(i) for i in newstr.split()]
print(listOfNumbers)
