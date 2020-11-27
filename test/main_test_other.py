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


if __name__ == '__main__':
    unittest.main()
