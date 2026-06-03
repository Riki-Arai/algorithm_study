N, X = map(int, input().split())
X_lists = [tuple(map(int, input().split())) for _ in range(N)]

dp_list = [False]*(X+1)
dp_list[0] = True
for i in range(N):
    m_list = []
    a, b = X_lists[i]
    for k in range(b, 0, -1):
        m_list.append(a*k)

    for j in range(X, -1, -1):
        if dp_list[j]:
            for m in m_list:
                if j+m < X+1:
                    dp_list[j+m] = True

if dp_list[X]:
    print("Yes")
else:
    print("No")