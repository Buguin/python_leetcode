import unittest
from common11.SolutionOther import Solution


class MyTestCase(unittest.TestCase):

    def test_fourSumCount(self):
        """
        454. 四数相加 II
        """
        A = [1, 2]
        B = [-2, -1]
        C = [-1, 2]
        D = [0, 2]
        ans = Solution.fourSumCount(A,B,C,D)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_reversePairs(self):
        """
        493. 翻转对
        """
        nums = [1,3,2,3,1]
        # nums = [2, 4, 3, 5, 1]
        nums = [5,4,3,2,1]
        ans = Solution.reversePairs(nums)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_maxRepeating(self):
        """
        5557. 最大重复子字符串
        """
        sequence = "ababc"
        word = "ab"
        ans = Solution.maxRepeating(sequence, word)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
