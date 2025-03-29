N = int(input())
a_list = list(map(int, input().split()))
not_pos_list = [a for a in a_list if a <= 0]
not_pos_num = N - len(not_pos_list)

res = 0
while not_pos_num > 1:
    a_list.sort(reverse=True)
    a_list[0] = a_list[0] - 1
    a_list[1] = a_list[1] - 1
    res += 1

    not_pos_list = [a for a in a_list if a <= 0]
    not_pos_num = N - len(not_pos_list)

print(res)