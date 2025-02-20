# February 14th, 2025
# Spiro Kontossoros
# Python unittest file
# This is a testing file for app.py.

import unittest

from app.Lab3_Spiro_Nathan import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestCircleArea(unittest.TestCase):
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")



    def tearDown(self):
        print()

    def tearDownClass(cls):
        print("tearDownClass")