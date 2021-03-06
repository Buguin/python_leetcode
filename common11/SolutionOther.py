# -*- coding:utf-8 -*-
# __author__ = 'Buguin'

from common11.Common import ListNode
import bisect
import collections


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

    @staticmethod
    def firstUniqChar(s: str) -> int:
        s_list = list(s)
        remain_counter = collections.Counter(s_list)
        for (key, value) in remain_counter.items():
            if value == 1:
                index = s_list.index(key)
                return index
        return -1

    @staticmethod
    def candy1(ratings: [int]) -> int:
        # 暴力
        size = len(ratings)
        if size == 0: return 0
        ans = []
        temp_ratings = []
        for i in range(size):
            rating = ratings[i]
            temp_ratings.append(rating)
            if not ans:
                ans.append(1)
                continue
            if temp_ratings[-2] < temp_ratings[-1]:
                ans.append(ans[-1] + 1)
            elif temp_ratings[-2] == temp_ratings[-1]:
                ans.append(1)
            else:
                ans.append(1)
                for j in range(len(temp_ratings) - 1,0, -1):
                    if temp_ratings[j] < temp_ratings[j - 1] and ans[j] >= ans[j - 1]:
                        ans[j - 1] += 1
                    else:
                        break
        return sum(ans)

    @staticmethod
    def candy2(ratings: [int]) -> int:
        size = len(ratings)
        if size == 0: return 0
        ans = []
        for i in range(size):
            if not ans:
                ans.append(1)
                continue
            if ratings[i - 1] < ratings[i]:
                ans.append(ans[-1] + 1)
            else:
                ans.append(1)
        ratings.reverse()
        ans.reverse()
        for i in range(size - 1):
            if ratings[i] < ratings[i + 1] and ans[i] >= ans[i + 1]:
                ans[i + 1] = ans[i] + 1
        ans.reverse()
        return sum(ans)

    @staticmethod
    def candy(ratings: [int]) -> int:
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret

    @staticmethod
    def findContentChildren(g: [int], s: [int]) -> int:
        g.sort()
        s.sort()
        num = 0
        while g:
            g_s = g.pop(0)
            if s:
                bi_index = bisect.bisect_left(s, g_s)
                if len(s) != bi_index:
                    s.pop(bi_index)
                    num += 1
                else:
                    break
            else:
                return num
        return num

    @staticmethod
    def findContentChildren2(g: [int], s: [int]) -> int:
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count

    @staticmethod
    def rotate(matrix: [[int]]) -> None:
        size_c = len(matrix[0]) - 1
        size_r = len(matrix)
        j_index = len(matrix[0])
        for i in range(size_r//2):
            j_index -= 1
            for j in range(i, j_index):
                temp1 = matrix[i][j]
                temp2 = matrix[j][size_c - i]
                temp3 = matrix[size_c - i][size_c - j]
                temp4 = matrix[size_c - j][i]
                matrix[i][j] = temp4
                matrix[j][size_c - i] = temp1
                matrix[size_c - i][size_c - j] = temp2
                matrix[size_c - j][i] = temp3
        # print(matrix)
        # return temp_max

    @staticmethod
    def isIsomorphic1(s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        if size_s != size_t: return False
        s_t_key = {}
        t_s_key = {}
        for s_char, t_char in zip(s,t):
            if s_char not in s_t_key.keys():
                s_t_key[s_char] = t_char
            if t_char not in t_s_key.keys():
                t_s_key[t_char] = s_char
            if s_t_key[s_char] != t_char or t_s_key[t_char] != s_char:
                return False
        return True

    @staticmethod
    def isIsomorphic2(s: str, t: str) -> bool:
        size_s = len(s)
        size_t = len(t)
        if size_s != size_t: return False
        for i in range(size_t):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True

    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        s_c = collections.Counter(list(s))
        t_c = collections.Counter(list(t))
        if len(s_c.keys()) != len(t_c.keys()):
            return False
        else:
            return True

    @staticmethod
    def minDistance(houses: [int], k: int) -> int:
        houses.sort()
        size = len(houses)
        if size == k :return 0
        cost_a = [[0]*size for _ in range(size)]
        for l in range(size-2,-1,-1):
            for r in range(l+ 1, size):
                cost_a[l][r] = houses[r] - houses[l] + cost_a[l+1][r-1]
        print(cost_a)
        ans_a = [[0] * (k+1) for _ in range(size + 1)]
        for i in range(1,size + 1):
            ans_a[i][1] = cost_a[0][i-1]
        for m in range(2,k+1):
            for n in range(m + 1, size + 1):
                ans_a[n][m] = float('inf')
                for p in range(m-1,n):
                    ans_a[n][m] = min(ans_a[n][m], ans_a[p][m-1] + cost_a[p+1-1][n-1])
        return ans_a[size][k]

    @staticmethod
    def minPatches1(nums: [int], n: int) -> int:
        ans = 0
        if len(nums) == 0:
            nums.append(1)
            ans += 1

        def find_num(f_nums: [int], num: int) -> int:
            temp = num
            if temp in f_nums:
                return 0
            f_index = []
            while temp and 0 not in f_index:
                index = min(bisect.bisect_right(f_nums, temp)-1, len(f_nums) - 1)
                if index in f_index:
                    index -= 1
                f_index.append(index)
                temp -= f_nums[index]
            if 0 not in f_index or temp == 0:
                return 0
            else:
                return num
        for i in range(1, n+1):
            temp_num = find_num(nums, i)
            if temp_num:
                ans += 1
                bisect.insort_left(nums, temp_num)
        return ans

    @staticmethod
    def minPatches(nums: [int], n: int) -> int:
        furthest = i = ans = 0
        while furthest < n:
            # 可覆盖到，直接用前缀和更新区间
            if i < len(nums) and nums[i] <= furthest + 1:
                furthest += nums[i] #  [1, furthest] -> [1, furthest + nums[i]]
                i += 1
            else:
                # 不可覆盖到，增加一个数 furthest + 1，并用前缀和更新区间
                furthest = 2 * furthest + 1 # [1, furthest] -> [1, furthest + furthest + 1]
                ans += 1
        return ans

    @staticmethod
    def lastStoneWeight(stones: [int]) -> int:
        stones.sort()
        while len(stones) > 1:
            temp1 = stones.pop(-1)
            temp2 = stones.pop(-1)
            if temp1 != temp2:
                temp = temp1 - temp2
                bisect.insort_left(stones, temp)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
