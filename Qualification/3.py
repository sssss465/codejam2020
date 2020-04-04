import sys, collections
import bisect
# parenting partnering returns
cin = sys.stdin.readline
cases = int(cin()) 

class Interval:
    def __init__(self, start, end):
       self.start = start
       self.end = end
    def __str__(self):
        return "(" + str(self.start) + " "+ str(self.end) + ")"
def overlap(int1, int2):
    return (int1.start < int2.end and int1.end > int2.start)

for case in (range(1, cases+1)):
    intervals = []
    for i in range(int(cin())):
        s = cin()
        s = [int(j) for j in s.rstrip().split(' ')]
        intervals.append(Interval(*s))
    res = ""
    d = []
    i = 0
    joe, bob = [0]*2000, [0]*2000
    #for j in intervals: print(j)
    while i < len(intervals):
        cur = intervals[i]
        if (1 not in joe[cur.start:cur.end]):
            res += "J"
            joe[cur.start:cur.end] = [1]*(cur.end -cur.start)
            print(joe[cur.start:cur.end])
        elif (1 not in bob[cur.start:cur.end]):
            res += "C"
            bob[cur.start:cur.end] = [1]*(cur.end -cur.start)
        else:
            res = "IMPOSSIBLE"
            break
        i += 1

    print("Case #" + str(case) + ":", res)
