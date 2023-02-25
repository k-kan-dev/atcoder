import numpy as np

def  binary_tree(l, s, e):
    if l[(s-e)//2]:
        return binary_tree(l, s, (s-e)//2)
    else:
        return binary_tree(l, (s-e)//2, e)


n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(int(np.sqrt(n)) + 1):
    for j in range(int(np.sqrt(n)) + 1):
        try:
            a.remove(int((np.sqrt(n) + 1))* i+j)
            ans += 1
        except ValueError:
            break

print(ans)
