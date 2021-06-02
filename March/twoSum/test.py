import unittest

from twoSum import twoSum

class TestSolution(unittest.TestCase):

    def testHello(self):
        nums = [2, 7, 11, 15]
        target = 9

        expectedOutput = [0, 1]
        actualOutput = twoSum(nums, target)

        self.assertEqual(expectedOutput, actualOutput)

if __name__ == '__main__':
    unittest.main()