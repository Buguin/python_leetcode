# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:

    def fib(self, N: int) -> int:
        """
        递归，记忆化自底向上
        :param N: 
        :return: 
        """
        if (N <= 1):
            return N

        current = 0
        prev1 = 0
        prev2 = 1

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N + 1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current

    def memoize(self, N: int) -> int:
        if N in self.cache_dict.keys():
            return self.cache_dict[N]
        self.cache_dict[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)

    def fib2(self, N: int) -> int:
        """
        递归，记忆化自顶向下
        :param N: 
        :return: 
        """
        self.cache_dict = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> int:
        if N in self.cache_dict.keys():
            return self.cache_dict[N]
        self.cache_dict[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)


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