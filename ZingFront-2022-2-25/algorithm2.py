"""
编程题：（⾮斐波那契数列⽅式）起初⼀对兔⼦，每4个⽉性成熟后⽣育下⼀对兔⼦，那么请问
理想状态下，第10个⽉总共有多少对兔⼦，如果是5个⽉才性成熟，24个⽉后⼜是多少？可以思考是
否有通⽤型算法；（tip:类和数组）
"""


class Solution:
    @classmethod
    def f(cls, initial=1, i: int=0, j: int=0):
        """
        :param initial: 最开始有 initial 对兔子
        :param i: i月性成熟后生育
        :param j: j月
        :return:
        """
        assert i > 0
        if j <= i:
            return initial

        # child 表示新出生的兔子，parent表示已成为父母的兔子，group表示正在发育中的兔子
        child, group, parent = [], [], []
        for _ in range(i):
            group.append(initial)
            child.append(0)
            parent.append(0)

        group.append(0)
        child.append(initial)
        parent.append(initial)

        for k in range(i+1, j+1):
            gk = child[k-1] + group[k-1] - child[k-i]
            pk = parent[k-1] + child[k-i]
            ck = parent[k-1] + child[k-i]
            group.append(gk)
            parent.append(pk)
            child.append(ck)
        return child[-1] + parent[-1] + group[-1]


if __name__ == '__main__':
    r = Solution.f(1, 2, 7)
    print(r)
