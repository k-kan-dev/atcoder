if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    n2 = n
    count = 1
    p = 0
 
    while(n2 != 0):
 
        ktop = int(n2 - k + 1)
        if(ktop > 0):
            p += ktop / n * 1 / count
            n2 -= ktop
 
        k /= 2
        count *= 2
        
    print(p)