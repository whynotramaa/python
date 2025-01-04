# multiplication table printer but skip 5th iteration

n = int(input("multiplication table for ? "))

for i in range(0,11):
    if i == 5:
        continue
    print( n, "*", i, n*i )
