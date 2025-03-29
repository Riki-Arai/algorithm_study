N = int(input())
A_list = list(map(int, input().split()))

for i in range(2, N):
    if A_list[i-2] * A_list[i] != A_list[i-1] * A_list[i-1]:
        print("No")
        exit()
print("Yes")