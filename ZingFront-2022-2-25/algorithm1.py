"""
某俱乐部有4只⾜球队A、B、C、D队，现按照1⾄20的级别划分每个队伍，⽬前每队的战⽃⼒⽔
平级别依次为10、7、5、4。现俱乐部为了优化各队的能⼒⽔平，决定每⽉底从战⽃⼒战⽃最⾼的队
伍抽出部分⼈⼒资源，平均分配到其他⼩队（规则：分配3个战⽃⼒的⼈⼒资源出来到其他⼩队，所
以经过⼀个⽉的调整分配，各⼩队现在的战⽃⼒⽔平：7、8、6、5）
那么请问，经过五年的战⽃⼒优化调整后，哪个⼩队的战⽃⼒最⾼，为多少？请编程求解该问
题，并思考是否为最优解。同时能否有对应的算法可以快速得出对应的结果？
"""


class Solution:
    """
    这种数据存在周期性，找到周期值，取余就行。
    """
    @classmethod
    def f(cls, initial: list=None, n: int=0):
        initial_len = len(initial)

        while n > 0:
            max_val = max(initial)
            index_val = initial.index(max_val)
            for i in range(initial_len):
                if i == index_val:
                    initial[i] -= 3
                else:
                    initial[i] += 1
            n -= 1
        return initial


if __name__ == '__main__':
    r = Solution.f([10, 7, 5, 4], 5 * 12)
    print(r)
