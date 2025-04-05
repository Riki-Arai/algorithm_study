N = int(input())
A_list = list(map(int, input().split()))

res = 0
while list(map(lambda x: x > 0, A_list)).count(True) > 1:
    res += 1
    A_list.sort(reverse=True)
    A_list[0] -= 1
    A_list[1] -= 1

print(res)