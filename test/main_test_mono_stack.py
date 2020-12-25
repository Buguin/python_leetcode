import unittest
from common11.SolutionMonoStack import Solution


class MyTestCase(unittest.TestCase):

    def test_searchRange(self):
        """
        376. 摆动序列
        """
        # nums = [1,7,4,9,2,5]
        nums = [1, 7]
        nums = [3,3,3,2,5]
        ans = Solution.wiggleMaxLength(nums)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
