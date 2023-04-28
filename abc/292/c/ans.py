n = int(input())

nl = [1] * (n + 1)

for i in range(2, n):
    for j in range(i, n + 1, i):
        nl[j] += 1

ans = 0
for i in range(1, n):
    ans += nl[i] * nl[n - i]

print(ans)
