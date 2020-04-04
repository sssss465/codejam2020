import sys, collections
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
    orig = intervals[:]
    intervals = sorted(intervals, key=lambda k: k.start)
    mp = {}
    res = ""
    d = []
    i = 0
    joe, bob = -1, -1
    #for j in intervals: print(j)
    while i < len(intervals):
        if joe == -1 or not overlap(intervals[joe], intervals[i]):
            res += "J"
            mp[intervals[i]] = "J"
            joe = i
        elif bob == -1 or not overlap(intervals[bob], intervals[i]):
            res += "C"
            mp[intervals[i]] = "C"
            bob = i
        else:
            res = "IMPOSSIBLE"
            break
        i += 1
    if res != "IMPOSSIBLE": 
        res = ''.join([mp[i] for i in orig])
    print("Case #" + str(case) + ":", res)

