n, q = map(int, input().split())
players = {}
for _ in range(q):
    e, x = map(int, input().split())

    if players.get(x) is None:
        players[x] = {
            "yellow": 0,
            "red": 0,
        }

    if e == 1:
        players[x]["yellow"] += 1
    elif e == 2:
        players[x]["red"] += 1
    elif e == 3:
        if (players[x]["yellow"] >= 2 or 
           players[x]["red"] >= 1):
            print("Yes")
        else:
            print("No")
