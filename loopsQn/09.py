items = ["apple", "banana", "orange", "mango"]
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

for i in items:
    if items.count(i) > 1:
        print(i)
        break
    
# otehr logic is create a set as it take snon duplicate items only so 
# check if item is in the set or not, if it is then print item and break otherwise .add(item)