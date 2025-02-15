import string

n = int(input())
list_ = [input().strip() for _ in range(n)]
t_point, h_point = 0, 0
a_list = list(string.ascii_lowercase)
for input_ in list_:
    t_score, h_score = 0, 0
    t_card, h_card = input_.split()
    if t_card == h_card:
        t_point += 1
        h_point += 1
        continue

    not_done_flag = True
    for x, y in zip(t_card, h_card):
        if a_list.index(x) > a_list.index(y):
            t_point += 3
            not_done_flag = False
            break
        elif a_list.index(x) < a_list.index(y):
            h_point += 3
            not_done_flag = False
            break

    if not_done_flag:
        if len(t_card) > len(h_card):
            t_point += 3
        else:
            h_point += 3

print(t_point, h_point)
