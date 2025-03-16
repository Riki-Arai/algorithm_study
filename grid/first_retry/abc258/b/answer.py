N = int(input())
A_list = [input() for _ in range(N)]

# 上、右上、右、右下、下、左下、左、左上
move_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
max_a_list = []
for i in range(N):
    for j in range(N):
        for m in move_list:
            max_a = ""
            max_a += A_list[i][j] 
            ii, jj = i, j
            for _ in range(N-1):
                ii = (ii + m[0]) % N
                jj = (jj + m[1]) % N
                max_a += A_list[ii][jj]

            max_a_list.append(int(max_a))

print(max(max_a_list))