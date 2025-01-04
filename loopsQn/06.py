# factorial calculator 
n = int(input("factorial for ? "))

# 5! = 5 * 4! =  * 3!
fact = 1 
while n > 0:
    fact = n * fact
    n = n-1
print(fact)
