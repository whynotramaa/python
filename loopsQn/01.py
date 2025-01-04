numbers = [1, -2, 3, -4, 5, 6, 6, -7, -8, 9, 10]
li = []
for num in numbers:
    if num>0 :
        if num in li:
            continue
        li.append(num)

print(li)