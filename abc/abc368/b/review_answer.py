N = int(input())
a_list = list(map(int, input().split()))

pos_num = N - len([a for a in a_list if a <= 0])
res = 0
while pos_num > 1:
    a_list.sort(reverse=True)
    a_list[0] -= 1
    a_list[1] -= 1
    res += 1

    pos_num = N - len([a for a in a_list if a <= 0])

print(res)