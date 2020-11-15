import unittest
from common11.Solution import Solution


class MyTestCase(unittest.TestCase):
    """
    239. 滑动窗口最大值
    """
    def test_maxSlidingWindow(self):
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
