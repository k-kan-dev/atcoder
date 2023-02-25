n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(min(k,n)):
    try:
        a.remove(i)
        ans += 1
    except ValueError:
        break

print(ans)
