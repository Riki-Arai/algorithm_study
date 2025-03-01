N = int(input())

re_list = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    re_list.append(A + B)

for re in re_list:
    print(re)
