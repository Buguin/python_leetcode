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
