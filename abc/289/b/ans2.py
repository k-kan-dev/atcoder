n, m = map(int, input().split())
am = list(map(int, input().split()))

string = list(range(1, n+1))
not_am = set(string[:-1]) - set(am)

ans = []; tmp = []
for i, s in enumerate(string):
    tmp.append(str(s))
    if (s in not_am) or (i == len(string)-1):
        tmp = reversed(tmp)
        ans.extend(tmp)
        tmp = []

print(" ".join(ans))
