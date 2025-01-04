# Problem: Given a string, find the first non-repeated character.

string = "aejdbbsajdb"

for char in string:
    if string.count(char) == 1:
        print("first non repeated character is : ", char)
        break