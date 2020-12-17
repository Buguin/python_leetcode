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
        ans = Solution.fourSumCount(A, B, C, D)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_reversePairs(self):
        """
        493. 翻转对
        """
        nums = [1, 3, 2, 3, 1]
        # nums = [2, 4, 3, 5, 1]
        nums = [5, 4, 3, 2, 1]
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
        list1 = [0, 1, 2, 3, 4, 5, 6]
        list2 = [1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009]
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

    def test_largestPerimeter(self):
        """
        976. 三角形的最大周长
        """
        nums = [200, 100, 100, 1, 1]
        ans = Solution.largestPerimeter(nums)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_removeKdigits(self):
        """
        402 移掉K位数字
        """
        nums = "10200"
        k = 1
        nums = "10"
        k = 2
        nums = "1234567890"
        k = 9
        ans = Solution.removeKdigits(nums, k)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_countPrimes(self):
        """
        204. 计数质数
        2  [4]
        3  [4,6,9]
        4  [4,6,9,8]
        5  [4,6,9,8,10,25]
        6  [4,6,9,8,10,25,12]
        7  [4,6,9,8,10,25,12,14,49]
        8  [4,6,9,8,10,25,12,14,49,16]
        9  [4,6,9,8,10,25,12,14,49,16,18]
        10 [4,6,9,8,10,25,12,14,49,16,18,20]
        11 [4,6,9,8,10,25,12,14,49,16,18,20,121]
        12 [4,6,9,8,10,25,12,14,49,16,18,20,121,24]
        """
        k = 100
        ans = Solution.countPrimes(k)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_generate(self):
        """
        118. 杨辉三角
        """
        k = 5
        # k = 0
        # k = 1
        ans = Solution.generate(k)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_matrixScore(self):
        """
        861. 翻转矩阵后的得分
        """
        A = [[0, 0, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 0]]
        A = [[1, 1, 1, 1],
             [1, 0, 0, 1],
             [1, 1, 1, 1]]
        ans = Solution.matrixScore(A)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_uniquePaths(self):
        """
        62. 不同路径
        """
        m = 3
        n = 2
        ans = Solution.uniquePaths(m, n)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_containsDuplicate(self):
        """
        217. 存在重复元素
        """
        nums = [1,2,3,1]
        ans = Solution.containsDuplicate(nums)
        print(ans)
        self.assertEqual(True, True)

    def test_groupAnagrams(self):
        """
        49. 字母异位词分组
        """
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        ans = Solution.groupAnagrams(strs)
        print(ans)
        self.assertEqual(True, True)

    def test_leastInterval(self):
        """
        621. 任务调度器
        """
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        ans = Solution.leastInterval(tasks, n)
        print(ans)
        self.assertEqual(True, True)

    def test_monotoneIncreasingDigits(self):
        """
        738. 单调递增的数字
        """
        N = 10
        N = 1234
        N = 332
        ans = Solution.monotoneIncreasingDigits(N)
        print(ans)
        self.assertEqual(True, True)

    def test_wordPattern(self):
        """
        290. 单词规律
        """
        pattern = "abba"
        str = "dog cat cat dog"
        # pattern = "abba"
        # str = "dog dog dog dog"
        # pattern = "abba"
        # str = "dog cat cat fish"
        # pattern = "aba"
        # str = "dog cat cat"
        pattern = "aaa"
        str = "aa aa aa aa"
        ans = Solution.wordPattern(pattern, str)
        print(ans)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
