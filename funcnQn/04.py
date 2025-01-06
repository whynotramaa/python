# Problem: Create a function that returns both the area and circumference of a circle given its radius.

def areaxcirc(radius):
    area = 3.14 * (radius**2)
    circum=2 * 3.14 * radius
    return area,circum

print(areaxcirc(5))