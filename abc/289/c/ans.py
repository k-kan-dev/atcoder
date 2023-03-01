import sys

n, m = map(int, input().split())
ci = []; si = []
for i in range(m):
    c = int(input())
    ci.append(c)
    s = set(map(int, input().split()))
    si.append(s)

d = {}
for i in range(1, n+1):
    d[i] = 0
    for s in si:
        if i in s:
            d[i] += 1

dv = d.values()
if 0 in dv:
    print(0)
    sys.exit()

print(sum(dv) - len(dv) + 1)
