#Has a function to calculate the circumference of a circle
import math


def find_circumference():
    radius = input("What is the radius of the circle? ")
    circumference = 2 * math.pi * int(radius)
    return circumference

find_circumference()