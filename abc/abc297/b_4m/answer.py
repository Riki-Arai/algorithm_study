S = input().strip()

b_x, b_y = [i for i, x in enumerate(list(S), 1) if x == "B"]
if b_x % 2 == b_y % 2:
    print("No")
    exit()


r_x, r_y = [i for i, x in enumerate(list(S)) if x == "R"]
if r_x < S.index("K") < r_y:
    print("Yes")
else:
    print("No")