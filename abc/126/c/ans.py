def calc(p, v, criteria):
    if v >= criteria:
        return p
    else:
        return calc(p/2, v*2, criteria)

n, k = map(int, input().split())

# init
sub = n - k + 1
p = 0
if sub > 0:
    p = sub / n

# calc p
for i in range(min(n, k-1)):
    p += 1/n * calc(1, i+1, k)

print("{:.9f}".format(p))
