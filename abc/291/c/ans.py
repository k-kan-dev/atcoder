import sys

n = int(input())
x = input()

s = set()
d = {
    "R": (0, 1),
    "L": (0, -1),
    "U": (1, 0),
    "D": (-1, 0)
}

current = [0, 0]
s.add(tuple(current))
for a in x:
    current[0] += d[a][0]
    current[1] += d[a][1]
    if (t := tuple(current)) in s:
        print("Yes")
        sys.exit(0)
    s.add(t)
print("No")
