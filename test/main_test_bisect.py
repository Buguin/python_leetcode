import unittest
from common11.SolutionBisect import Solution


class MyTestCase(unittest.TestCase):

    def test_fourSumCount(self):
        """
        454. 四数相加 II
        """
        nums = [5, 7, 7, 8, 8, 10]
        target = 7
        nums = [1,1]
        target = 0
        # nums = [5,7,7,8,8,10]
        # target = 6
        nums = [2,2]
        target = 2
        ans = Solution.searchRange(nums, target)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
