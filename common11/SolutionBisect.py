# -*- coding:utf-8 -*-
# __author__ = 'Buguin'
import bisect


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

    @staticmethod
    def maxNumber(nums1: [int], nums2: [int], k: int) -> [int]:

        def delete_m_max(nums, m) -> [int]:
            size = len(nums)
            remain = size - m
            nums_r = []
            for n in nums:
                while nums_r and m and nums_r[-1] < n:
                    nums_r.pop(-1)
                    m -= 1
                nums_r.append(n)
            return nums_r[:remain]

        def merge(ans1_m: [int], ans2_m: [int]) -> [int]:
            ans_m = []
            size_ans1 = len(ans1_m)
            size_ans2 = len(ans2_m)
            n = 0
            m = 0
            if ans1_m[n] > ans2_m[m]:
                ans_m.append(ans1_m[n])
                n += 1
            else:
                ans_m.append(ans2_m[m])
                m += 1


            return ans_m

        ans = [0]
        for i in range(k):
            ans1 = delete_m_max(nums1, i)
            ans2 = delete_m_max(nums2, k-i)
            ans_t = merge(ans1, ans2)
            if ans_t.__str__() >ans.__str__():
                ans = ans_t
        return ans
