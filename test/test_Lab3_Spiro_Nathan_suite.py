import unittest
# from unittest import suite
from test.test_Lab3_Spiro_Nathan import TestArea


def shape_test_suite():
    run_tests = True
    user_input = ""
    # You can add individual test methods to the suite too
    # suite.addTest(TestEmployee('test_email'))

    while run_tests:
        user_input = input("Please enter one of the following options:\n- "
                           "'c' for testing area of circle\n- "
                           "'t' for testing area of trapezium\n- "
                           "'e' for testing area of ellipse\n- "
                           "'r' for testing area of rhombus\n- "
                           "'q' to quit\n"
                           "What would you like to do?: ")

        shape_suite = unittest.TestSuite()
        if user_input == 'c':
            shape_suite.addTest(TestArea('test_circle_01'))
            shape_suite.addTest(TestArea('test_circle_02'))
            shape_suite.addTest(TestArea('test_circle_03'))
            shape_suite.addTest(TestArea('test_circle_04'))
            shape_suite.addTest(TestArea('test_circle_05'))
            runner = unittest.TextTestRunner()
            print(runner.run(shape_suite))
        elif user_input == 't':
            shape_suite.addTest(TestArea('test_trapezium_01'))
            shape_suite.addTest(TestArea('test_trapezium_02'))
            shape_suite.addTest(TestArea('test_trapezium_03'))
            shape_suite.addTest(TestArea('test_trapezium_04'))
            shape_suite.addTest(TestArea('test_trapezium_05'))
            runner = unittest.TextTestRunner()
            print(runner.run(shape_suite))
        elif user_input == 'e':
            shape_suite.addTest(TestArea('test_ellipse_01'))
            shape_suite.addTest(TestArea('test_ellipse_02'))
            shape_suite.addTest(TestArea('test_ellipse_03'))
            shape_suite.addTest(TestArea('test_ellipse_04'))
            shape_suite.addTest(TestArea('test_ellipse_05'))
            runner = unittest.TextTestRunner()
            print(runner.run(shape_suite))
        elif user_input == 'r':
            shape_suite.addTest(TestArea('test_rhombus_01'))
            shape_suite.addTest(TestArea('test_rhombus_02'))
            shape_suite.addTest(TestArea('test_rhombus_03'))
            shape_suite.addTest(TestArea('test_rhombus_04'))
            shape_suite.addTest(TestArea('test_rhombus_05'))
            runner = unittest.TextTestRunner()
            print(runner.run(shape_suite))
        elif user_input == 'q':
            print("Exiting Program")
            run_tests = False
        else:
            print("Error: Invalid input, please try again")


if __name__ == '__main__':
    shape_test_suite()
