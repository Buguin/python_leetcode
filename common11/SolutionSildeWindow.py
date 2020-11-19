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
    def maxSlidingWindow1(nums, k) -> [int]:
        size = len(nums)
        m_left = [0]*size
        m_left[0] = nums[0]
        m_right = [0]*size
        m_right[-1] = nums[-1]
        m_ans = []
        for i in range(1, size):
            if i % k == 0:
                m_left[i] = nums[i]
            else:
                m_left[i] = max(m_left[i-1], nums[i])
            j = size - i - 1
            if (j + 1) % k == 0:
                m_right[j] = nums[j]
            else:
                m_right[j] = max(m_right[j+1], nums[j])
        for m in range(k, size + 1):
            res = max(m_left[m - 1], m_right[m - k])
            m_ans.append(res)
        return m_ans
