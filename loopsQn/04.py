# reverse a string but using loop
string = input("What string you want to get reversed ? ")
rev_str = ""
for i in string:
    rev_str = i + rev_str
    
print(rev_str)
