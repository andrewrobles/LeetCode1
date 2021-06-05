import unittest

from solution import solution

class TestSolution(unittest.TestCase):

    def testHello(self):
        expected = 'Hello world'
        actual = solution()

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()