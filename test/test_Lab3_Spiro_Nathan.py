# February 14th, 2025
# Spiro Kontossoros
# Python unittest file
# This is a testing file for app.py.

# NOW DOES THIS WORK?

import unittest
from app.Lab3_Spiro_Nathan import ShapeArea


class TestCircleArea(unittest.TestCase):
    def setUpClass(self):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def test_circle_01(self):
        """Test areas when radius = 5"""
        self.assertEqual(78.54, ShapeArea.circle_area(self, 5))

    def tearDown(self):
        print("End of test: ", self.shortDescription())

    def tearDownClass(self):
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()