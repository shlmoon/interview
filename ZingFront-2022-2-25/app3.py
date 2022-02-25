"""
给定数组A[4,6,3,8...](长度为n)，现随机给⼀个同样长度n的⼀个随机数组B，将B按照给定数组
A相邻数字⼤⼩关系进⾏排列，从所有符合排列的数组中筛选相邻差的绝对值之和最⼤的那些数组。
"""


class Solution:
    """
    核心使用是回溯，剪枝
    """
    @classmethod
    def f(cls, l1: list=None, l2: list=None):
        l_len, res = len(l1), []

        def dfs(lst=None, temp=None):
            lt_len, temp_len = len(lst), len(temp)

            if temp_len == l_len:
                res.append(temp)
                return

            for i in range(lt_len):
                lt = lst[::]
                curr = lt.pop(i)
                if not temp:
                    dfs(lst=lt, temp=[curr])

                else:
                    prev, nst = l1[temp_len-1], l1[temp_len]
                    tail = temp[-1]
                    if prev == nst:
                        if curr == tail:
                            dfs(lst=lt, temp=temp + [curr])
                        else:
                            temp.pop(-1)
                    else:
                        check1 = prev > nst
                        check2 = tail > curr
                        if check1 is check2:
                            dfs(lst=lt, temp=temp + [curr])
                        else:
                            temp.pop(-1)

        dfs(lst=l2, temp=[])
        res_abs = [sum(abs(temp[_] - temp[_ + 1]) for _ in range(l_len - 1)) for temp in res]
        max_result = max(res_abs)
        idx_list = [i for i in range(len(res_abs)) if res_abs[i] == max_result]
        return [res[_] for _ in idx_list]


if __name__ == '__main__':
    t = Solution.f([6, 7, 5, 8, 9], [1, 2, 3, 4, 5])
    print(t)
