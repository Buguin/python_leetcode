# -*- coding:utf-8 -*-
# __author__ = 'Buguin'

import bisect
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __new__(cls, nums: []):
    #     temp1 = ListNode()
    #     for i in range(1,len(nums)):
    #         temp2 = ListNode(nums[i])
    #         temp1.next = temp2
    #     return temp1


class Solution:
    # 贪心算法

    @staticmethod
    def maxProfit( prices: [int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
