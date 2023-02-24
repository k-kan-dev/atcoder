s = input()

ans = ["MMYY", "YYMM", "AMBIGUOUS", "NA"]

pre = int(s[:2])
post = int(s[2:])

is_pre_month = is_post_month = False

# preprocess
if pre >= 1 and pre <= 12 :
    is_pre_month = True    
if post >= 1 and post <= 12:
    is_post_month = True

# judge
if is_pre_month:
    if is_post_month:
        t = 2
    else:
        t = 0
else:
    if is_post_month:
        t = 1
    else:
        t = 3

print(ans[t])
