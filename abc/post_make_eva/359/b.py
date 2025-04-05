N = int(input())
a_list = list(map(int, input().split()))

res = 0
for i in range(N*2):
    if i + 2 < N*2 and a_list[i] == a_list[i+2]:
        res += 1

print(res)
