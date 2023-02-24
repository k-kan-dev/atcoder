from decimal import Decimal


def calc(p, v, criteria, times):
    if v >= criteria:
        return 1 / p
    else:
        return calc(p/2, v*2, criteria, times+1)

n, k = map(int, input().split())

# init
sub = n - k + 1
p = 0
if sub > 0:
    p = Decimal(sub/n)

# calc p
t = 0; frac = Decimal(0.0)
for i in range(min(n,k-1)):
    t = calc(1, i+1, k, 1)
    frac += Decimal(1 / int(t))

p += Decimal(1/n) * frac
print("{:.9f}".format(float(p)))
