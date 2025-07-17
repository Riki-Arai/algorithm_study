N = int(input())

a_list, b_list = [], []
sum_a = 0
for _ in range(N):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    sum_a += a

res = 0
for i in range(N):
    res = max(sum_a - a_list[i] + b_list[i], res)

print(res)