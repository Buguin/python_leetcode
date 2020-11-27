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

