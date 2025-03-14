R, C = map(int, input().split())
b_list = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if b_list[i][j] not in (".", "#"):
            b = int(b_list[i][j])
            b_list[i][j] = "."
            for k in range(R):
                for l in range(C):
                    if abs(k - i) + abs(l - j) <= b and b_list[k][l] == "#":
                        b_list[k][l] = "."


for b in b_list:
    print("".join(b))
