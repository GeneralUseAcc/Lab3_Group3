# Date: February 18th, 2025
# Authors: Spiro Kontossoros, Nathan Sheldrake
# Student IDs: 100843569 (Kontossoros), 100964827 (Sheldrake)
# Description: A program for calculating the area of various shapes.

from math import pi


def circle_area(r):
    """Calculates the area of a circle given the radius"""
    return pi * (r ** 2)

def trapezium_area(a, b, h):
    """Calculates the area of a trapezium given base A, base B and the height"""
    return ((a+b)/2)*h

def ellipse_area():
    """Calculates the area of a circle given the radius"""

def rhombus_area():
    """Calculates the area of a circle given the radius"""

# Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circles with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))