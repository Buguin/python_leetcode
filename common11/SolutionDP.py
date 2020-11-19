# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:
    memo = []
    memo_index = []

    def fib(self, N: int) -> int:
        """
        递归，带备忘录
        :param N: 
        :return: 
        """
        if N in self.memo_index:
            return self.memo[self.memo_index.index(N)]
        if N == 0:
            self.memo_index.append(0)
            self.memo.append(0)
            return 0
        elif N == 1:
            self.memo_index.append(1)
            self.memo.append(1)
            return 1
        ans = self.fib(N - 1) + self.fib(N - 2)
        self.memo_index.append(N)
        self.memo.append(ans)
        return ans

    @staticmethod
    def fib1(N: int) -> int:
        """
        递归
        :param N: 
        :return: 
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        return Solution.fib(N - 1) + Solution.fib(N - 2)

    @staticmethod
    def longestPalindrome(s: str) -> str:
        size = len(s)
        ans = []
        beg_w = 0
        for end_w in range(size):
            beg_str = s[beg_w]
            # if

    @staticmethod
    def partition(s: str) -> [[str]]:
        size = len(s)
        ans = []
        beg_w = 0
        for end_w in range(size):
            beg_str = s[beg_w]
            # if