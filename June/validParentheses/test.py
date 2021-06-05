import unittest

from solution import solution

class TestSolution(unittest.TestCase):

    def test1(self):
        s = "()"
        expected = True
        actual = solution(s)

        self.assertEqual(expected, actual)

    def test2(self):
        s = "()[]{}"
        expected = True
        actual = solution(s)

        self.assertEqual(expected, actual)

    def test3(self):
        s = "(]"
        expected = False
        actual = solution(s)

        self.assertEqual(expected, actual)

    def test4(self):
        s = "([)]"
        expected = False
        actual = solution(s)

        self.assertEqual(expected, actual)

    def test5(self):
        s = "{[]}"
        expected = True
        actual = solution(s)

        self.assertEqual(expected, actual)

    def test5(self):
        s = "["
        expected = False
        actual = solution(s)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()