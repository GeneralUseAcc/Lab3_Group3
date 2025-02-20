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
        if user_input == 'c':
            shape_suite.addTest(TestArea('test_circle_01'))
            # You can make suite of entire test class too
            shape_suite.addTest(unittest.makeSuite(TestArea))
            runner = unittest.TextTestRunner()
            print(runner.run(shape_suite))





shape_test_suite()
