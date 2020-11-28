# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:

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

    @staticmethod
    def reversePairs(nums: [int]) -> int:
        # def find_index(num, dums_sort) -> int:
        #     med = len(dums_sort) // 2
        #     if num == dums_sort[med]:
        #         return med
        #     elif num < dums_sort[med]:
        #         find_index(num, dums_sort[0:med])
        #     else:
        #         find_index(num, dums_sort[med:])
        #     return 0
        # 哈希表
        ans = 0
        size = len(nums)
        d_nums = []
        for num in nums:
            d_nums.append(num*2)
        for i in range(size):
            temp_dums = d_nums[i+1:]
            temp_dums.sort()
            while temp_dums:
                temp_dum = temp_dums.pop(-1)
                if temp_dum < nums[i]:
                    ans += len(temp_dums) + 1
                    break
        return ans

    @staticmethod
    def reversePairs1(nums: [int]) -> int:
        # 暴力
        ans = 0
        size = len(nums)
        for i in range(size):
            for j in range(i+1, size):
                if nums[i] > 2*nums[j]:
                    ans += 1
        return ans

