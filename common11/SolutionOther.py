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

    @staticmethod
    def creatLN(nums: [int]) -> ListNode:
        # 暴力
        ls = ListNode(nums[0])
        temp = ListNode(nums[1])
        ls.next = temp
        for i in range(2,len(nums)):
            temp_t = ListNode(nums[i])
            temp.next = temp_t
            temp = temp_t
        return ls

    @staticmethod
    def maxRepeating(sequence: str, word: str) -> int:
        # 暴力
        size = len(sequence)
        size_word = len(word)
        ans = 0
        while sequence:
            temp_ans = 0
            if word in sequence:
                index_s = sequence.index(word)
                sequence = sequence[index_s:]
                for i in range(0, len(sequence), size_word):
                    if sequence[i:i+size_word] == word:
                        temp_ans += 1
                        continue
                    else:
                        break
                sequence = sequence[size_word*temp_ans:]
            else:
                break
            ans = max(ans, temp_ans)
        return ans

    @staticmethod
    def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 暴力
        first = ListNode([0])
        first.next = list1
        first1 = list1
        i = 0
        while first.next is not None:
            if i == a:
                first.next = list2
                break
            first = first.next
            first1 = first1.next
            i += 1
        j = i
        while first1.next is not None:
            first1 = first1.next
            if j == b:
                while True:
                    if list2.next is not None:
                        list2 = list2.next
                    else:
                        list2.next = first1
                        break
                break
            j +=1
        return list1

    @staticmethod
    def largestPerimeter(A: [int]) -> int:
        # 暴力 两边之和大于另一边
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0
        # size = len(A)
        # A.sort(reverse=True)
        # ans = 0
        # for i in range(size):
        #     for j in range(i+1, size):
        #         for k in range(j+1,size):
        #             a = A[i]
        #             b = A[j]
        #             c = A[k]
        #             if a + b > c and a + c > b and b + c > a:
        #                 ans = a + b + c
        #                 return ans
        # return ans

    @staticmethod
    def largestPerimeter1(A: [int]) -> int:
        # 合并两边？？？
        size = len(A)
        A.sort(reverse=True)
        ans = 0
        merge_bide = []
        for i in range(size):
            for j in range(i+1, size):
                temp_list1 = A[i] + A[j]
                temp_list2 = abs(A[i] - A[j])
                merge_bide.append([temp_list1, temp_list2])
        for n in range(size):
            temp_merge_bide = merge_bide[size - 1:]

            for m in range(len(merge_bide)):

                if merge_bide[m][0] > A[n] > merge_bide[m][1]:
                    ans = merge_bide[m][0] + A[n]
                    return ans
        return ans

    @staticmethod
    def maxNumber(nums1: [int], nums2: [int], k: int) -> [int]:
        # 合并两边？？？
        size_nums1 = len(nums1)
        size_nums2 = len(nums2)
        ans = []
        # 比较两个数字的头

        return ans

    @staticmethod
    def removeKdigits(num: str, k: int) -> str:
        size = len(num)
        num_int = []
        remain = size - k
        if remain <= 0:
            return "0"
        for n in num:
            # while k and stack and stack[-1] > digit:
            while k > 0 and num_int and num_int[-1] > n:
                num_int.pop()
                k -= 1
            num_int.append(n)
        # 去除左边的0
        while num_int:
            if num_int[0] == '0' and len(num_int) > 1:
                num_int.pop(0)
            else:
                break
        ans = ''.join(num_int[:remain])
        return ans

    @staticmethod
    def countPrimes1(n: int) -> int:
        # 暴力
        if n <= 2:
            return 0
        ans = 1
        prime_flag = True
        temp_list = [2]
        for i in range(3, n, 2):
            for t in temp_list:
                if i % t == 0:
                    prime_flag = False
                    break
                prime_flag = True
            if prime_flag:
                ans += 1
            temp_list.append(i)
        return ans

    @staticmethod
    def countPrimes(n: int) -> int:
        # 数乘
        if n <= 2:
            return 0
        ans = 0
        temp_list = []
        for i in range(2, n):
            if i not in temp_list:
                ans += 1
                bisect.insort_left(temp_list, i * 2)
                bisect.insort_left(temp_list, i * i)
            else:
                bisect.insort_left(temp_list, i * 2)
        return ans

    @staticmethod
    def generate1(numRows: int) -> [[int]]:
        # 数乘
        ans = []
        for i in range(1, numRows + 1):
            if i == 1:
                temp_list = [1]
            else:
                temp_list = [1]*i
            size = len(temp_list)
            for j in range(1, size - 1):
                temp_list[j] = ans[i - 2][j - 1] + ans[i - 2][j]
            ans.append(temp_list)
        return ans

    @staticmethod
    def generate2(numRows: int) -> [[int]]:
        # 数乘
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(2, numRows + 1):
            temp_list = [1]*i
            size = len(temp_list)
            if size % 2 == 1:
                range_s = size // 2 + 1
            else:
                range_s = size // 2
            for j in range(1, range_s):
                temp_list[j] = ans[i - 2][j - 1] + ans[i - 2][j]
                temp_list[size - 1 - j] = ans[i - 2][j - 1] + ans[i - 2][j]
            ans.append(temp_list)
        return ans

    @staticmethod
    def generate(numRows: int) -> [[int]]:
        # 数乘
        if numRows == 0:
            return []
        ans = [[1]]
        while len(ans) < numRows:
            temp_list = []
            for a, b in zip([0] + ans[-1], ans[-1] + [0]):
                temp_list.append(a+b)
            ans.append(temp_list)
        return ans

    @staticmethod
    def matrixScore(A: [[int]]) -> int:
        # 数乘
        n, m = len(A), len(A[0])
        res = n

        for i in range(1, m):
            res <<= 1
            s = sum([A[j][i] ^ A[j][0] for j in range(n)])
            res += max(s, n - s)
        return res

    @staticmethod
    def uniquePaths1(m: int, n: int) -> int:
        sub = n + m - 2
        res = 1
        for i in range(1, m):
            res = res * (sub - (m - 1) + i) // i
        return res

    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        print(f)
        return f[m - 1][n - 1]

    @staticmethod
    def containsDuplicate1(nums: [int]) -> bool:
        size = len(nums)
        nums_temp = collections.Counter(nums)
        size_diff = len(nums_temp.keys())
        if size == size_diff:
            return False
        else:
            return True

    @staticmethod
    def containsDuplicate(nums: [int]) -> bool:
        nums_temp = {}
        for num in nums:
            if num in nums_temp.keys():
                return True
            else:
                nums_temp[num] = 1
        return False

    @staticmethod
    def groupAnagrams(strs: [str]) -> [[str]]:
        strs_temp = {}
        for str in strs:
            str_list = list(str)
            str_list.sort()
            str_temp = ''.join(str_list)
            if str_temp in strs_temp.keys():
                strs_temp[str_temp].append(str)
            else:
                strs_temp[str_temp] = [str]
        ans = list(strs_temp.values())
        # print(ans)
        return ans

    @staticmethod
    def leastInterval(tasks: [str], n: int) -> int:
        freq = collections.Counter(tasks)

        # 任务总数
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            time = max(time, minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best == -1 or rest[j] > rest[best]:
                        best = j

            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time

    @staticmethod
    def monotoneIncreasingDigits(N: int) -> int:
        ones = 111111111
        result = 0
        for _ in range(9):
            while result + ones > N:
                ones //= 10
            result += ones
        return result

    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        patterns = []
        strs = []
        for i in range(len(s_list)):
            if not patterns or (pattern[i] not in patterns and s_list[i] not in strs):
                patterns.append(pattern[i])
                strs.append(s_list[i])
                continue
            else:
                if pattern[i] in patterns:
                    index = patterns.index(pattern[i])
                    if strs[index] != s_list[i]:
                        return False
                else:
                    index = strs.index(s_list[i])
                    if patterns[index] != pattern[i]:
                        return False
        return True

    @staticmethod
    def findTheDifference1(s: str, t: str) -> str:
        s_map = collections.Counter(s)
        t_map = collections.Counter(t)
        if len(s) > len(t):
            for key, value in s_map.items():
                if key in t_map.keys():
                    if t_map[key] > s_map[key]:
                        return key
                else:
                    return key
        else:
            for key, value in t_map.items():
                if key in s_map.keys():
                    if t_map[key] > s_map[key]:
                        return key
                else:
                    return key

    @staticmethod
    def findTheDifference2(s: str, t: str) -> str:
        max_num = 0
        for s_t in s:
            max_num += ord(s_t)
        for t_t in t:
            max_num -= ord(t_t)
        str_c = chr(abs(max_num))
        return str_c

    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        max_num = 0
        for s_t in s:
            max_num ^= ord(s_t)
        for t_t in t:
            max_num ^= ord(t_t)
        str_c = chr(max_num)
        return str_c

    @staticmethod
    def removeDuplicateLetters1(s: str) -> str:
        stack = []
        seen = set()
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in seen:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)

    @staticmethod
    def removeDuplicateLetters(s: str) -> str:
        stack = []
        # seen = set()
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)
