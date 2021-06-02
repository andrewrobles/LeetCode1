import unittest

class TestSolution(unittest.TestCase):

    def testHello(self):

        expected = 'Hello world'
        actual = 'Hello world'

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()