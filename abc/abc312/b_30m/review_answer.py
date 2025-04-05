N, M = map(int, input().split())
A_lists = [list(input()) for _ in range(N)] # 取得例:[["#","#"], [".","."]・・・["#","#"]]

for i in range(N):
    for j in range(M):
        for k in range(4):
            if k != 3 and i + k < N and "".join(A_lists[i+k][j:j+4]) == "###.":
                continue
            elif k  == 3 and i + k < N and "".join(A_lists[i+k][j:j+4]) == "....":
                continue
            else:
                break
        else:
            ii = i + 5
            jj = j + 5
            for k in range(4):
                if k == 0 and ii + k < N and "".join(A_lists[ii+k][jj:jj+4]) == "....":
                    continue
                elif k  != 0 and ii + k < N and "".join(A_lists[ii+k][jj:jj+4]) == ".###":
                    continue
                else:
                    break
            else:
                print(i+1, j+1)