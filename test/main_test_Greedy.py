import unittest
from common11.SolutionGreedy import Solution


class MyTestCase(unittest.TestCase):

    def test_maxProfit(self):
        """
        714. 买卖股票的最佳时机含手续费
        """
        nums = [1,3,1,2,0,5]
        k = 3
        ans = Solution.maxProfit(nums, k)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
