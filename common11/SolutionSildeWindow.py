# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:

    @staticmethod
    def maxSlidingWindow(nums, k) -> [int]:
        class MyQueue:
            def __init__(self):
                self.m_stack = []

            def pop(self, value):
                if len(self.m_stack) != 0 and value == self.m_stack[0]:
                    self.m_stack.pop(0)

            def push(self, value):
                while len(self.m_stack) != 0 and value > self.m_stack[-1]:
                    self.m_stack.pop(-1)
                self.m_stack.append(value)

            def front(self):
                return self.m_stack[0]
        size = len(nums)
        que = MyQueue()
        m_ans = []
        for i in range(k):
            que.push(nums[i])
        m_ans.append(que.front())
        for i in range(k, size):
            que.pop(nums[i - k])
            que.push(nums[i])
            m_ans.append(que.front())
        return m_ans

    @staticmethod
    def fourSumCount( A:[int], B: [int], C: [int], D: [int]) -> int:
        sum_a_b = {}
        for a in A:
            for b in B:
                temp_sum = a + b
                sum_a_b[temp_sum] = sum_a_b.get(temp_sum, 0) + 1
                # if temp_sum not in sum_a_b.keys():
                #     sum_a_b[temp_sum] = 1
                # else:
                #     sum_a_b[temp_sum] += 1
        ans = 0
        for c in C:
            for d in D:
                temp_sum = c + d
                if -temp_sum in sum_a_b:
                    ans += sum_a_b[-temp_sum]
                # if -temp_sum in sum_a_b.keys():
                #     ans += sum_a_b[-temp_sum]
        return ans
