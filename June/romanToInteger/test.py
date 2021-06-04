import unittest

from solution import romanToInteger 

class TestSolution(unittest.TestCase):

    def test_III(self):
        s = 'III'

        expected = 3
        actual = romanToInteger(s)

        self.assertEqual(expected, actual)
    
    def test_IV(self):
        s = 'IV'

        expected = 4
        actual = romanToInteger(s)

        self.assertEqual(expected, actual)

    def test_IX(self):
        s = 'IX'

        expected = 9
        actual = romanToInteger(s)

        self.assertEqual(expected, actual)

    def test_LVIII(self):
        s = 'LVIII'

        expected = 58
        actual = romanToInteger(s)

        self.assertEqual(expected, actual)
    
    def test_MCMXCIV(self):
        s = 'MCMXCIV'

        expected = 1994
        actual = romanToInteger(s)

        self.assertEqual(expected, actual)
    
    def test_XL(self):
        s = 'XL'

        expected = 40
        actual = romanToInteger(s)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()