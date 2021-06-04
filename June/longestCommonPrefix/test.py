import unittest

from longestCommonPrefix import longestCommonPrefix

class TestSolution(unittest.TestCase):

    def testFl(self):
        strings = ["flower","flow","flight"]

        actual = longestCommonPrefix(strings)
        expected = "fl"
        
        self.assertEqual(expected, actual)
    
    def testNone(self):
        strings = ["dog","racecar","car"]

        actual = longestCommonPrefix(strings)
        expected = ""
        
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()