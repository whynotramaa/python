# Problem: Check if a number is prime.

n = 49

# logic for prime --> divide by 1 or self, start from 2 and end before number 
is_prime = True
for i in range(2,n):
    if(n%i == 0):
        is_prime = False
    else: 
       continue
print(is_prime)