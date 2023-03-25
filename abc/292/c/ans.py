n = int(input())

def get_num_of_divisors(x):
    upper_divisors, lower_divisiors = set(), set()
    i = 1
    while i ** 2 <= x:
         if x % i == 0:
            lower_divisiors.add(i)
            if (x // i) != i:
                upper_divisors.add(x//i)
         i += 1
    return len(lower_divisiors | upper_divisors)

ans = 0
for ni in range(1, n//2 + 1):
    ab = get_num_of_divisors(ni)
    cd = get_num_of_divisors(n-ni)
    if ni == n//2 and n % 2 == 0:
        ans += ab * cd
    else:
        ans += ab * cd * 2

print(ans)
