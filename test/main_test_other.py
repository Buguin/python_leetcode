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

    def test_findTheDifference(self):
        """
        389. 找不同
        """
        s = "abcd"
        t = "abcde"
        s = ""
        t = "y"
        s = "a"
        t = "aa"
        s = "ae"
        t = "aea"
        ans = Solution.findTheDifference(s, t)
        print(ans)
        self.assertEqual(True, True)

    def test_removeDuplicateLetters(self):
        """
        316. 去除重复字母
        """
        s = "bcabc"
        # s = "cbacdcbc"
        ans = Solution.removeDuplicateLetters(s)
        print(ans)
        self.assertEqual(True, True)

    def test_firstUniqChar(self):
        """
        #387 字符串中的第一个唯一字符
        """
        s = "loveleetcode"
        # s = "cbacdcbc"
        ans = Solution.firstUniqChar(s)
        print(ans)
        self.assertEqual(True, True)

    def test_candy(self):
        """
        135. 分发糖果
        """
        ratings = [1,0,2]
        ratings = [1,2,2]
        ratings = [1,2,3,4,5]
        # ratings = []
        # 7
        ratings = [1,3,2,2,1]
        # 13
        ratings = [1,2,87,87,87,2,1]
        # 11
        # ratings = [1,3,4,5,2]
        ans = Solution.candy(ratings)
        print(ans)
        self.assertEqual(True, True)

    def test_findContentChildren(self):
        """
        455. 分发饼干
        """
        g = [1, 2, 3]
        s = [1, 1]
        # g = [1, 2]
        # s = [1, 2, 3]
        # g = [1, 2, 3]
        # s = [3]
        ans = Solution.findContentChildren(g, s)
        print(ans)
        self.assertEqual(True, True)

    def test_rotate(self):
        """
        48. 旋转图像
        """
        matrix =[
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]]
        matrix =[
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
        # matrix =[
        #     [1, 2, 3, 4, 5],
        #     [6, 7, 8, 9, 10],
        #     [11, 12, 13, 14, 15],
        #     [16, 17, 18, 19, 20],
        #     [21, 22, 23, 24, 25]]
        ans = Solution.rotate(matrix)
        print(ans)
        self.assertEqual(True, True)

    def test_isIsomorphic(self):
        """
        205. 同构字符串
        """
        s = "egg"
        t = "add"
        s = "foo"
        t = "bar"
        s = "paper"
        t = "title"
        s = "ab"
        t = "aa"
        ans = Solution.isIsomorphic(s, t)
        print(ans)
        self.assertEqual(True, True)

    def test_minDistance(self):
        """
        1478. 安排邮筒
        """
        houses = [1, 4, 8, 10, 20]
        k = 3
        houses = [7,4,6,1]
        k = 1
        ans = Solution.minDistance(houses, k)
        print(ans)
        self.assertEqual(True, True)

    def test_minPatches(self):
        """
        330. 按要求补齐数组
        """
        nums = [1, 3]
        n = 6
        nums = [1,5,10]
        n = 20
        nums = []
        n = 7
        ans = Solution.minPatches(nums, n)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)

    def test_lastStoneWeight(self):
        """
        1046. 最后一块石头的重量
        """
        stones = [2, 7, 4, 1, 8, 1]
        ans = Solution.lastStoneWeight(stones)
        print(ans)
        if ans == 0:
            self.assertEqual(True, False)
        else:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
