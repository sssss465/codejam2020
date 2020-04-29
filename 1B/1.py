import sys
import collections
import bisect
import math
# parenting partnering returns
cin = sys.stdin.readline
cases = int(cin())


def solve(l, r):
    cache = {}
    dirs = [[0, 1, 'N'], [0, -1, 'S'], [-1, 0, 'W'], [1, 0, 'E']]
    if (l % 2 != 0 and r % 2 != 0):
        return 'IMPOSSIBLE'

    def bfs(end, pos=(0, 0), jmp=1, path=[]):
        q = collections.deque()
        q.append((0, 0, 1, ""))
        its = 100000
        i = 0
        # print(q)
        while len(q) > 0:
            if i == its:
                return "IMPOSSIBLE"
            i += 1
            p = q.popleft()
            if (p[0], p[1]) == end:
                return p[3]
            jp = p[2]
            arr = p[3]
            for x, y, d in dirs:
                a = jp * x
                b = jp * y
                q.append((a+p[0], b+p[1], jp*2, arr + d))
        return "IMPOSSIBLE"

    def dfs(end, pos=(0, 0), jmp=1, path=[]):
        if pos in cache:
            return cache[pos]
        if pos == end:
            cache[pos] = ''.join(path)
            return ''.join(path)
        res = None
        for x, y, d in dirs:
            a = jmp * x
            b = jmp * y
            r = dfs(end, (a, b), jmp*2, path + [d])
            if res == None:
                res = r
            else:
                res = r if len(r) < len(res) else res
        cache[pos] = res
        return res
    return bfs((l, r))


for i in range(1, cases+1):
    c = cin()
    l, r = (int(i) for i in c.split(' '))
    print("Case #" + str(i) + ":", solve(l, r))
