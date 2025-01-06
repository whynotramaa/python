# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def kwargs_check(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
# key : value

kwargs_check(name="ojha", gaali="madharchod")
kwargs_check(name="atish", gaali="gaandu")
kwargs_check(gaali="gaandu")

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_kwargs(name="shaktiman", power="lazer")
# print_kwargs(name="shaktiman")
# print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")