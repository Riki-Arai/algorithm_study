R, C = map(int, input().split())
A_lists = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if A_lists[i][j] not in (".", "#"):
            for k in range(R):
                for l in range(C):
                    if int(A_lists[i][j]) >= abs(k - i) + abs(l - j) and A_lists[k][l] == "#":
                        A_lists[k][l] = "."
            A_lists[i][j] = "." 

for a in A_lists:
    print("".join(a))