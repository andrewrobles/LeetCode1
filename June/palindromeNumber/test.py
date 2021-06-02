import unittest

from solution import palindromeNumber

class TestSolution(unittest.TestCase):

    def testHello(self):
        x = 121

        expected = True
        actual = palindromeNumber(x)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()