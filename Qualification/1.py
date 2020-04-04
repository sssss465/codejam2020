import sys, collections
# vestigium
cnt = 0
cin = sys.stdin.readline

cases = int(cin()) 

def solve(mat):
    rows = [set() for i in range(len(mat))]
    cols = [set() for i in range(len(mat[0]))]
    trace = 0
    def dups(mat):
        cnt = 0
        for i in range(len(mat)):
            s = set()
            for j in range(len(mat[0])):
                if mat[i][j] in s:
                    cnt += 1
                    break
                s.add(mat[i][j])
        return cnt
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == j:
                trace += mat[i][j]
    return (trace, dups(mat), dups([*zip(*mat)]))
for case in (range(1, cases+1)):
    size = int(cin())
    m = []
    for i in range(size):
        row = cin()
        row = [int(i) for i in row.split(' ')]
        m.append(row)
    print('Case #' + str(case) + ':', *solve(m))
