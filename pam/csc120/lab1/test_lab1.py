'''CSC120 201609 Lab 1 unit tests.

@author lungj
'''
import unittest

try:
    import triangle as sub
except Exception:
    pass

def find_function():
    # Get functions defined in the submission.
    submission_functions = {k: v for (k, v) in sub.__dict__.items() if not k.startswith('__') and callable(v)}
    
    # Preferentially try triangle_area and calculate_area as the function to test.
    if 'triangle_area' in submission_functions:
        return submission_functions['triangle_area']

    if 'calculate_area' in submission_functions:
        return submission_functions['calculate_area']
        
    if len(submission_functions) == 0:
        return None
    
    # Return a random function.
    return list(submission_functions.values())[0]
        
class TestAreaCalculator(unittest.TestCase):
    def test_F00_was_submitted(self):
        ''' Testing to see if any submission was made at all.'''

        self.assertTrue(sub != None, 'No submission was found. Did you use the correct file name?')

    def test_F01_any_function(self):
        ''' Testing to see if any functions were defined.'''

        self.assertTrue(find_function() != None, 'No functions were defined')

    def test_F02_function_name(self):
        ''' Testing to see if the function name was correct.'''
        fn = find_function()
        if not fn:
            self.assertTrue(False, 'No functions were defined')
        
        self.assertTrue(fn.__name__ == 'triangle_area' or fn.__name__ == 'calculate_area', 'Function name should have been triangle_area or calculate_area.')

    def test_F03_function_name(self):
        ''' Testing to see if the function accepts the correct number of arguments.'''
        fn = find_function()
        if not fn:
            self.assertTrue(False, 'No functions were defined')
        
        try:
            fn(1)
            self.assertTrue(False, 'Function header has the wrong number of parameters -- "def x(parameter1, parameter2, parameter3, ...):".')
        except TypeError:
            pass        

        try:
            fn(1, 2, 3)
            self.assertTrue(False, 'Function header has the wrong number of parameters -- "def x(parameter1, parameter2, parameter3, ...):".')
        except TypeError:
            pass        

        try:
            fn(1, 2)
        except TypeError:
            self.assertTrue(False, 'Function header has the wrong number of parameters -- "def x(parameter1, parameter2, parameter3, ...):".')


    def test_F04_normal_case(self):
        ''' Testing to see if the function works on a normal test case.'''
        fn = find_function()

        # These are exactly representable as floating point numbers.
        self.assertEqual(fn(9.5, 6.5), 30.875, 'Area of a triangle not calculated correctly.')

if __name__ == '__main__':
    unittest.main()
