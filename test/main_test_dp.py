import unittest
from common11.SolutionDP import Solution


class MyTestCase(unittest.TestCase):

    def test_partition(self):
        """
        131. 分割回文串
        :return: 
        """
        s = "aab"
        ans = Solution.partition(s)
        print(ans)
        if len(ans) == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_longestPalindrome(self):
        """
        5. 最长回文子串
        :return: 
        """
        s = "aab"
        ans = Solution.longestPalindrome(s)
        print(ans)
        if len(ans) == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_fib(self):
        """
        509. 斐波那契数
        :return: 
        """
        input_num = 3
        s = Solution()
        ans = s.fib(input_num)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_coinChange(self):
        """
        322. 零钱兑换
        :return: 
        """
        coins = [1, 2, 5]
        amount = 11
        ans = Solution.coinChange(coins, amount)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()
