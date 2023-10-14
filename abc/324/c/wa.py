
n, T = input().split()
n = int(n)

def search(t, s):
    del_start = False
    del_end = False
    pre_s = s[:len(s)//2]
    post_s = s[len(s)//2:]
    if t.startswith(pre_s):
        del_start = True
        s = s[len(pre_s):]
        try:
            t = t[len(pre_s):]
        except:
            t = ""
        if len(post_s) <= 1:
            return 0

    if t.endswith(post_s):
        del_end = True
        s = s[:-len(post_s)]
        try:
            t = t[: - len(post_s)]
        except:
            t = ""
        if len(pre_s) <= 1:
            return 0

    if del_start == del_end:
        if len(t) > 1 or len(s) > 1:
            return 1
        else:
            return 0 
    else:
        if del_start:
            return search(t, post_s)        
        elif del_end:
            return search(t, pre_s)


ans = []
for i in range(1, n+1):
    count = 1
    # input
    S = input()

    # check
    if search(T, S) == 0:
        pass
    else:
        continue

    # ans
    ans.append(str(i))

print(len(ans))
print(" ".join(ans))
