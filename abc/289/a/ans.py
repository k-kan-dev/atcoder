s = input()
d = {
    "1": "0",
    "0": "1"
}
ans = [d[x] for x in s]
print("".join(ans))