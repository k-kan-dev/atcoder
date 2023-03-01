n, m = map(int, input().split())
am = list(map(int, input().split()))

string = list(range(1, n+1))
separators = []
for s in string[:-1]:
    if s not in am:
        separators.append(s)

ans = []; tmp = []
for s in string:
    if s not in separators:
        tmp.append(str(s))
    else:
        tmp.append(str(s))
        tmp = reversed(tmp)
        ans.extend(tmp)
        tmp = []
if tmp != []:
    tmp = reversed(tmp)
    ans.extend(tmp)

print(" ".join(ans))
