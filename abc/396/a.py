N = int(input())
a_list = list(map(int, input().split()))

for i in range(N-2):
    if a_list[i] == a_list[i+1] and a_list[i+1] == a_list[i+2]:
        print("Yes")
        exit()

print("No")
