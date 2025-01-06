# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    # print(args)
    for i in args:
        print(i ** 2)
    print("")
    return sum(args)

print(sum_all(1,2,3,45,6,43,42,32,2))