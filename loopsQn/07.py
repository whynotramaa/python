# Problem: Keep asking the user for input until they enter a number between 1 and 10.

n = int(input("Enter a number betweeen 1 and 10 "))

while (n<0 or n>10):
    n = int(input("Enter a number betweeen 1 and 10 "))

print("Thank You")