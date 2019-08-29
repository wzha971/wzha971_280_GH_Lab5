import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        # Arrange
        result = maths.add(2, 3)
        result1 = maths.add(1,0)
        result2 = maths.add(-1,1)
        # Act
        
        # Assert
        self.assertEqual(result, 5)
        self.assertEqual(result1,1)
        self.assertEqual(result2,0)

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        pass # TODO

    def test_factorial(self):
        result = maths.factorial(9)
        self.assertEqual(result, 362880)
        
        result = maths.factorial(8)
        self.assertEqual(result,40320)

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
