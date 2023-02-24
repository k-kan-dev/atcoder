n, k = map(int, input().split())
s = str(input())

s = [x for x in s]
s[k-1] = s[k-1].lower()

print("".join(s))
