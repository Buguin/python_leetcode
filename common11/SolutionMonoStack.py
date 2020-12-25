# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:
    @staticmethod
    def wiggleMaxLength(nums: [int]) -> int:
        size = len(nums)
        # nums_temp = []
        # for i in range(size):
        #     nums_temp.append(nums[i+1] - nums[i])
        if len(nums) < 2: return len(nums)
        pre_diff = nums[1] - nums[0]
        if pre_diff == 0:
            ans = 1
        else:
            ans = 2
        for i in range(2, size):
            cur_diff = nums[i] - nums[i - 1]
            if (cur_diff > 0 and pre_diff <= 0) or (cur_diff < 0 and pre_diff >= 0):
                ans += 1
                pre_diff = cur_diff
        return ans

    @staticmethod
    def maximalRectangle(matrix: [[str]]) -> int:
        size_r = len(matrix)
        if not size_r: return 0
        size_c = len(matrix[0])
        ans = 0
        def maximalList(list_int: [int]) -> int:
            ans_l = 0
            mono_stack = []
            list_int = [-1] + list_int + [-1]
            for i in range(len(list_int)):
                while mono_stack and list_int[mono_stack[-1]] > list_int[i]:
                    hight = list_int[mono_stack.pop(-1)]
                    wight = i - mono_stack[-1] - 1
                    ans_l = max(ans_l, hight * wight)
                mono_stack.append(i)
            return ans_l
        matrix_list = [0] * size_c
        for i in range(size_r):
            for j in range(size_c):
                if int(matrix[i][j]):
                    matrix_list[j] += int(matrix[i][j])
                else:
                    matrix_list[j] = 0
            ans = max(ans, maximalList(matrix_list))
        return ans
