n, a, b = map(int, input().split())
ans = ["" for i in range(n*a)]

for i in range(n):
    for j in range(n*a):
        if (i+j//a)%2==0:
            ans[j] += "."*b
        else:
            ans[j] += "#"*b

for i in ans:
    print(i)



n, a, b = map(int, input().split())
ans = [[""]*n*b for _ in range(n*a)]

for i in range(n*a):
    for j in range(n*b):
        pos_i = i//a
        pos_j = j//b
        if (pos_i + pos_j) % 2 == 0:
            ans[i][j] = "."
        else:
            ans[i][j] = "#"

for i in ans:
    print("".join(map(str, i)))


## first
N, A, B = map(int, input().split())
res_lists = [["*"]*B*N for _ in range(A*N)]

v_count = 0
for i in range(0, N*A, A):
    w_count = 0
    for j in range(0, N*B, B):
        if v_count % 2 == 0:
            if w_count % 2 == 0:
                for a in range(A):
                    for b in range(B):
                        res_lists[i+a][j+b] = "."
            else:
                for a in range(A):
                    for b in range(B):
                        res_lists[i+a][j+b] = "#"
        else:
            if w_count % 2 == 0:
                for a in range(A):
                    for b in range(B):
                        res_lists[i+a][j+b] = "#"
            else:
                for a in range(A):
                    for b in range(B):
                        res_lists[i+a][j+b] = "."

        w_count += 1

    v_count += 1


for res_list in res_lists:
    print("".join(res_list))