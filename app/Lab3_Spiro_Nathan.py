# Date: February 18th, 2025
# Authors: Spiro Kontossoros, Nathan Sheldrake
# Student IDs: 100843569 (Kontossoros), 100964827 (Sheldrake)
# Description: A program for calculating the area of various shapes.

from math import pi
# DOES THIS WORK?


class ShapeArea(object):
    def circle_area(self, r):
        """Calculates the area of a circle given the radius"""
        if not isinstance(r, (int)):
            raise ValueError("Input must be an integer")
        elif (r <= 0):
            raise ValueError("Input cant be negative")
        return round(pi * (r ** 2), 2)

    def trapezium_area(self, a, b, h):
        """Calculates the area of a trapezium given base A, base B and the height"""
        if not isinstance(a, (int)):
            raise ValueError("Input must be an integer")
        elif not isinstance(b, (int)):
            raise ValueError("Input must be an integer")
        elif not isinstance(h, (int)):
            raise ValueError("Input must be an integer")
        elif (a or b or h <= 0):
            raise ValueError("Input cant be negative")
        return round(((( a + b ) / 2) * h), 2)

    def ellipse_area(self, a, b):
        """Calculates the area of an ellipse given a and b"""
        if not isinstance(a, (int)):
            raise ValueError("Input must be an integer")
        elif not isinstance(b, (int)):
            raise ValueError("Input must be an integer")
        elif (a or b <= 0):
            raise ValueError("Input cant be negative")
        return round((pi * a * b), 2)

    def rhombus_area(self, p, q):
        """Calculates the area of a rhombus given p and q"""
        if not isinstance(p, (int)):
            raise ValueError("Input must be an integer")
        elif not isinstance(q, (int)):
            raise ValueError("Input must be an integer")
        elif (p or q <= 0):
            raise ValueError("Input cant be negative")
        return round(((p * q) / 2), 2)



if __name__ == '__main__':
    shape = ShapeArea()

    # Test function
    # radii = [2, 0, -3, 2 + 5j, True, "radius"]
    radii = [5]
    message = "Area of circles with r = {radius} is {area}."

    for r in radii:
        A = shape.circle_area(r)
        print(message.format(radius=r, area=A))