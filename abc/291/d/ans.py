n = int(input())
al = []; bl = []
for _ in range(n):
    a, b = map(int, input().split())
    al.append(a)
    bl.append(b)

div = 998244353
all = 2**n
ans = 0 # 条件を満たすパターンのtotal

count = 0
ia, ib = (al[0], bl[0])
for aa, bb in zip(al[1:],bl[1:]):
    if ia == aa:
        count += 1
    if ia == bb:
        count += 1
        
        ia = aa
        ib = bb
        

print(ans%div)