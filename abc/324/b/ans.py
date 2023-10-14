import math
import sys
n = int(input())

memo = n
for i in range(int(math.sqrt(n))):

    if memo % 2 == 0:
        memo = memo / 2
    elif memo % 3 == 0:
        memo = memo / 3
    else:
        if memo == 1:
            break
        else:
            print("No")
            sys.exit()
            break
print("Yes")
