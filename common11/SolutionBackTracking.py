# -*- coding:utf-8 -*-
# __author__ = 'Buguin'


class Solution:

    def __init__(self):
        self.res = []

    def splitIntoFibonacci1(self, S: str) -> [int]:
        def subDigit(s_b: str, start: int, end: int):
            sub_d = 0
            for k in range(start, end):
                sub_d = sub_d * 10 + int(s_b[k])
            return sub_d

        def backTrack(s_b: str, index: int):
            # 边界条件判断，如果截取完了，并且res长度大于等于3，表示找到了一个组合。
            if index == len(s_b) and len(self.res) >= 3:
                return True
            for j in range(len(s_b)):
                if s_b[index] == '0' and j > index:
                    break
                num = subDigit(s_b, index, j + 1)
                size = len(self.res)
                # 如果截取的数字大于res中前两个数字的和，说明这次截取的太大，直接终止，因为后面越截取越大
                if size >= 2 and num > self.res[-1] + self.res[-2]:
                    break
                if size <= 1 or num == self.res[-1] + self.res[-2]:
                    # // 把数字num添加到集合res中
                    self.res.append(num)
                    # // 如果找到了就直接返回
                    if backTrack(s_b, j + 1):
                        return True
                    # // 如果没找到，就会走回溯这一步，然后把上一步添加到集合res中的数字给移除掉
                    self.res.pop(-1)
            return False
        backTrack(S, 0)
        return self.res

    def splitIntoFibonacci(self, S: str) -> [int]:
        n, up = len(S), 2147483647

        def get_list(start):
            # 判断前面两个数会不会超过上限
            if max(li) > up:
                return False

            # 遍历后面所有的字符串看看能不能组成斐波那契，
            # 如果 数超上限 或 最后一个数超字符串长度 或 字符串并不是下一个数 则直接跳出
            while start < n:
                now = li[-1] + li[-2]
                c = len(str(now))
                if now > up or start + c > n or int(S[start:start + c]) != now:
                    return False
                li.append(now)
                start += c
            return True

        for i in range(1, 11):
            # 这里让j取不到字符串末尾最后一位，顺便如果两个字符串有个是0开始的，直接只跑0的情况
            for j in range(1, min(11, n - i)):
                li = [int(S[:i]), int(S[i:i + j])]
                if get_list(i + j):
                    return li
                if S[i] == '0':
                    break
            if S[0] == '0':
                break
        return []
