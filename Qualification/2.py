import sys, collections
# nesting depth
cin = sys.stdin.readline
cases = int(cin()) 

for case in (range(1, cases+1)):
    a = cin().rstrip()
    res = ""
    depth = 0
    for c in a:
        if int(depth) == int(c): pass
        if int(depth) < int(c):
           res += "(" * (int(c)-int(depth)) + c
        else:
           res += ")" * abs(int(c)-int(depth))+c
        depth = int(c)
    if depth: res += ")"*depth
    print("Case #" + str(case) + ":", res)
