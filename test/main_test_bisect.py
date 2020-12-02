import unittest
from common11.SolutionBisect import Solution


class MyTestCase(unittest.TestCase):

    def test_searchRange(self):
        """
        34. 在排序数组中查找元素的第一个和最后一个位置
        """
        nums = [5, 7, 7, 8, 8, 10]
        target = 7
        nums = [1,1]
        target = 0
        # nums = [5,7,7,8,8,10]
        # target = 6
        nums = [2, 2]
        target = 2
        ans = Solution.searchRange(nums, target)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_maxNumber(self):
        """
        321. 拼接最大数
        """
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
        ans = Solution.maxNumber(nums1, nums2, k)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
