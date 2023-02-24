from fractions import Fraction


def calc(p, v, criteria, times):
    if v >= criteria:
        return times
    else:
        return calc(p/2, v*2, criteria, times*2)

n, k = map(int, input().split())

# init
sub = n - k + 1
p = 0
if sub > 0:
    p = Fraction(sub, n)

# calc p
t = 0; frac = Fraction(0, 1)
for i in range(min(n,k-1)):
    t = calc(1, i+1, k, 1)
    frac += Fraction(1, t)

p += Fraction(1, n) * frac
# print("{:.9f}".format(float(p)))
print(float(p))
