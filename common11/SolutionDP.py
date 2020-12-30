# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:
    @staticmethod
    def coinChange(coins: [int], amount: int) -> int:
        """
        动态规划，自顶向下
        :param coins: 
        :param amount: 
        :return: 
        """
        memo = {}
        def dp(n):
            if n in memo.keys():
                return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)
            if res != float('INF'):
                memo[n] = res
                return res
            else:
                memo[n] = -1
                return -1

        return dp(amount)

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

    @staticmethod
    def maxProfit(prices: [int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    @staticmethod
    def maxProfit1881(k: int, prices: [int]) -> int:
        if len(prices) <=1: return 0
        size_p = len(prices)
        profit = [[0]*2 for _ in range(size_p)]
        profit[0] = [-prices[0], 0]
        for i in range(1, size_p):
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] - prices[i])
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] + prices[i])
        # 获取差价
        temp_stack = []
        for m in range(1, size_p):
            if profit[m][1] > profit[m - 1][1]:
                temp_stack.append(profit[m][1] - profit[m-1][1])
        temp_stack.sort()
        ans = 0
        for n in range(min(k,len(temp_stack))):
            ans += temp_stack[n]
        return ans

    @staticmethod
    def maxProfit188(k: int, prices: [int]) -> int:
        if len(prices) <=1: return 0
        size_p = len(prices)
        sell = [[0]*k for _ in range(size_p)]
        buy = [[0] * k for _ in range(size_p)]
        buy[0][0] = -prices[0]
        sell[0][0] = 0
        for j in range(k):
            for i in range(j + 1, size_p):
                buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j-1]+ prices[i])
        return 0


