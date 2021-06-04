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
    
    def testEmpty(self):
        strings = [""]

        actual = longestCommonPrefix(strings)
        expected = ""
        
        self.assertEqual(expected, actual)
    
    def testDiffLengths(self):
        strings = ["ab", "a"]

        actual = longestCommonPrefix(strings)
        expected = "a"
        
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()