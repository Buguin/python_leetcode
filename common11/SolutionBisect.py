# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:

    @staticmethod
    def searchRange(nums: [int], target: int) -> [int]:
        # 二分法:判断数字边界
        def bisect_find(nums_m: [int], start: int, end: int) -> [int]:
            if start == end:
                if nums_m[start] == target:
                    return [start, end]
                else:
                    return [-1, -1]
            mid = (start + end)//2
            if nums_m[mid] < target:
                ans_m = bisect_find(nums_m, mid + 1, end)
            elif nums_m[mid] > target:
                ans_m = bisect_find(nums_m, start, mid)
            else:
                # 中间的场景
                ans_m = [-1, -1]
                for i in range(mid, -1, -1):
                    if nums_m[i] == target:
                        ans_m[0] = i
                    else:
                        break
                for j in range(mid, end + 1):
                    if nums_m[j] == target:
                        ans_m[1] = j
                    else:
                        break
            return ans_m
        if len(nums) == 0:
            return [-1, -1]
        ans = bisect_find(nums, 0, len(nums) - 1)
        return ans

    @staticmethod
    def searchRange1(nums: [int], target: int) -> [int]:
        # 二分法:判断到最小维度，即单个数字维度
        def bisect_find(nums_m: [int], start: int, end: int):
            mid = (start + end)//2
            if start == end:
                if nums_m[start] == target:
                    return [mid, mid]
                else:
                    return [-1, -1]
            # 左边的场景
            ans_left = bisect_find(nums_m, start, mid)
            # 右边的场景
            ans_right = bisect_find(nums_m, mid + 1, end)
            # 中间的场景
            # mid_ans = [-1, -1]
            # for i in range(mid, 0, -1):
            #     if nums_m[i] == target:
            #         mid_ans[0] = i
            #     else:
            #         break
            # for j in range(mid, end):
            #     if nums_m[j] == target:
            #         mid_ans[1] = j
            #     else:
            #         break
            ans_b = [-1, -1]
            if ans_left[1] + 1 == ans_right[0]:
                ans_b[0] = ans_left[0]
                ans_b[1] = ans_right[1]
            else:
                if ans_left[1] != -1 and ans_right[0] == -1:
                    ans_b = ans_left
                elif ans_left[1] == -1 and ans_right[0] != -1:
                    ans_b = ans_right
            return ans_b
        if target not in nums:
            return [-1, -1]
        ans = bisect_find(nums, 0, len(nums) - 1)
        return ans
