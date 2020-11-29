import unittest
from common11.SolutionOther import Solution
from common11.SolutionOther import ListNode


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

    def test_mergeInBetween(self):
        """
        5558. 合并两个链表
        """
        list1 = [0, 1, 2, 3, 4, 5, 6]
        list2 = [1000000, 1000001, 1000002]
        a = 3
        b = 4
        list1 = [0,1,2,3,4,5,6]
        list2 = [1000000,1000001,1000002,1000003,1000004,1000005,1000006,1000007,1000008,1000009]
        a = 2
        b = 5
        ls_list1 = Solution.creatLN(list1)
        ls_list2 = Solution.creatLN(list2)
        ans = Solution.mergeInBetween(ls_list1, a, b, ls_list2)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()
