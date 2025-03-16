N, M = map(int, input().split())
S_list = [input() for _ in range(N)]

target1 = ["###."] * 3 + ["...."]
target2 = ["...."] + [".###"] * 3
for i in range(N - 8):
    for j in range(M - 8):
        if [S[i + k][j : j + 4] for k in range(4)] == target1 and [
            S[i + k][j + 5 : j + 9] for k in range(5, 9)
        ] == target2:
            print(i + 1, j + 1)