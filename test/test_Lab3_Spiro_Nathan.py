# February 14th, 2025
# Spiro Kontossoros
# Python unittest file
# This is a testing file for app.py.

# NOW DOES THIS WORK?

import unittest
from app.Lab3_Spiro_Nathan import ShapeArea


class TestArea(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print("setUp")
        self.shape_tester = ShapeArea()

    def test_circle_01(self):
        """Test area when radius = 5"""
        self.assertEqual(self.shape_tester.circle_area(5), round(78.54, 2))

    def test_circle_02(self):
        """Test if float input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.circle_area, (5.5))

    def test_circle_03(self):
        """Test if negative input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.circle_area, (-5))

    def test_circle_04(self):
        """Test if input is 0"""
        self.assertRaises(ValueError, self.shape_tester.circle_area, (0))


    def test_trapezium_01(self):
        """Test area when bases = 10, 20 and height = 5 (valid case)"""
        self.assertEqual(self.shape_tester.trapezium_area(10, 20, 5), 75)

    def test_trapezium_02(self):
        """Test if float input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.trapezium_area, (10.5, 20, 5))

    def test_trapezium_03(self):
        """Test if negative input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.trapezium_area, (10, -20, 5))

    def test_trapezium_04(self):
        """Test if input is 0"""
        self.assertRaises(ValueError, self.shape_tester.trapezium_area, (0, 0, 0))


    def test_ellipse_01(self):
        """Test area when a = 7, b = 4 (valid case)"""
        self.assertEqual(self.shape_tester.ellipse_area(7, 4), round(28, 2))

    def test_ellipse_02(self):
        """Test if float input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.ellipse_area, (7.5, 4))

    def test_ellipse_03(self):
        """Test if negative input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.ellipse_area, (-7, 4))

    def test_ellipse_04(self):
        """Test if input is 0"""
        self.assertRaises(ValueError, self.shape_tester.ellipse_area, (0, 0))


    def test_rhombus_01(self):
        """Test area when diagonals = 8, 6 (valid case)"""
        self.assertEqual(self.shape_tester.rhombus_area(8, 6), 24)

    def test_rhombus_02(self):
        """Test if float input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.rhombus_area, (8.5, 6))

    def test_rhombus_03(self):
        """Test if negative input raises ValueError"""
        self.assertRaises(ValueError, self.shape_tester.rhombus_area, (8, -6))

    def test_rhombus_04(self):
        """Test if input is 0"""
        self.assertRaises(ValueError, self.shape_tester.rhombus_area, (0, 0))


    def tearDown(self):
        print("End of test: ", self.shortDescription())

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')



if __name__ == '__main__':
    unittest.main()