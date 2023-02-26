n, k = map(int, input().split())
a = set(map(int, input().split()))

a.discard(k)
sub = set(range(k+1)) - a
print(min(sub))
