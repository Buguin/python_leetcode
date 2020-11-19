# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:

    @staticmethod
    def fib(N: int) -> int:
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