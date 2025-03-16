N, M = map(int, input().split())
S_list = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        first_flag = False
        count = 0
        for k in range(4):
            if k == 3 and count == 3:
                if i+k < N and j+4 < M and S_list[i+k][j:j+4] == "....":
                    first_flag = True
            else:
                if i+k < N and j+4 < M and S_list[i+k][j:j+4] == "###.":
                    count += 1
        ii = i + 8
        jj = j + 8 
        if first_flag and ii < N and jj < M:
            count = 0
            for k in range(4):
                hoge = S_list[ii-k][jj-3:jj+1]
                fuga = count
                if k == 3 and count == 3:
                    if S_list[ii-k][jj-3:jj+1] == "....":
                        print(i+1, j+1)
                else:
                    if ii-k >= 0 and jj-4 >= 0 and S_list[ii-k][jj-3:jj+1] == ".###":
                        count += 1