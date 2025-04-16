N, M = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

c_list = sorted(A_list + B_list)
for i in range(len(c_list)-1):
    if c_list[i] in A_list and c_list[i+1] in A_list:
        print("Yes")
        exit()

print("No")