n, k = map(int, input().split())
s = input()

ans = ""; count = 0
for i in s:
    if i == "o" and count < k:
        count += 1
        ans += "o"
    else:
        ans += "x" 

print(ans)
