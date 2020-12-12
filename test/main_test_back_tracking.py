import unittest
from common11.SolutionBackTracking import Solution


class MyTestCase(unittest.TestCase):

    def test_splitIntoFibonacci(self):
        """
        842. 将数组拆分成斐波那契序列
        :return: 
        """
        s = "123456579"
        solution = Solution()
        ans = solution.splitIntoFibonacci(s)
        print(ans)
        if len(ans) == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
