import unittest
from common11.SolutionSildeWindow import Solution


class MyTestCase(unittest.TestCase):

    def test_maxSlidingWindow(self):
        """
        239. 滑动窗口最大值
        """
        nums = [1,3,1,2,0,5]
        k = 3
        ans = Solution.maxSlidingWindow(nums, k)
        print(ans)
        if len(ans) == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
