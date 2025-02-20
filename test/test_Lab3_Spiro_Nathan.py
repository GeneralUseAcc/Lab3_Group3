# February 14th, 2025
# Spiro Kontossoros
# Python unittest file
# This is a testing file for app.py.

# NOW DOES THIS WORK?

import unittest
from app.Lab3_Spiro_Nathan import ShapeArea


class TestCircleArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print("setUp")
        self.shape_tester = ShapeArea()

    def test_circle_01(self):
        """Test areas when radius = 5"""
        self.assertEqual(78.54, self.shape_tester.circle_area(5))

    def tearDown(self):
        print("End of test: ", self.shortDescription())

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')



if __name__ == '__main__':
    unittest.main()