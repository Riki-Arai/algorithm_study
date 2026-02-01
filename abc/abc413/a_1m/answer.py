N, M = map(int, input().split())
A_list = list(map(int, input().split()))

sum_ = sum(A_list)
if sum_ <= M:
    print("Yes")
else:
    print("No")