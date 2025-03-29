N, M = map(int, input().split())
A_list = list(map(int, input().split()))
X_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    sum_ = 0
    for x in X_list:
        sum_ += x[i]
    if sum_ < A_list[i]:
        print("No")
        exit()
print("Yes")