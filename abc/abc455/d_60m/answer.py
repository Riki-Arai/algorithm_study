import sys; sys.setrecursionlimit(10**7)

N, Q = map(int, input().split()) # 取得例：1 2

front_card_list = [-1]*(N+1)
back_card_list = [-1]*(N+1)
deck_list = [i for i in range(N+1)]
for _ in range(Q):
    C, P = map(int, input().split()) # 取得例：1 2
    if deck_list[C] == C:
        deck_list[C] = -1

    back_card_list[P] = C
    if front_card_list[C] == -1:
        front_card_list[C] = P
    else:
        back_card_list[front_card_list[C]] = -1
        front_card_list[C] = P

res_list = [0]*(N+1)
for d in deck_list[1:]:
    if d != -1:
        res = 1
        dd = d
        while back_card_list[dd] != -1:
            res += 1
            dd = back_card_list[dd]

        res_list[d] = res

print(*res_list[1:])