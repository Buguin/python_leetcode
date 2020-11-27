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
