import unittest
# from unittest import suite
from test.test_Lab3_Spiro_Nathan import TestArea


def shape_test_suite():
    run_tests = True
    shape_suite = unittest.TestSuite()
    user_input = ""
    # You can add individual test methods to the suite too
    # suite.addTest(TestEmployee('test_email'))

    while run_tests:
        user_input = input("Please enter one of the following options:\n- 'c' for testing area of circle\n- 't' for testing area of trapezium\n- 'e' for testing area of ellipse\n- 'r' for testing area of rhombus\n- 'q' to quit\nWhat would you like to do?: ")
        if user_input == 'c':
            shape_suite.addTest(TestArea('test_circle_01'))
            # You can make suite of entire test class too
            shape_suite.addTest(unittest.makeSuite(TestArea))
            runner = unittest.TextTestRunner()
            print(runner.run(shape_suite))


shape_test_suite()
