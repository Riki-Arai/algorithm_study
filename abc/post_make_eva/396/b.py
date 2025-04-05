N = int(input())

card_list = [0] * 100
for _ in range(N):
    q = list(map(int, input().split()))
    if q[0] == 1:
        card_list.append(q[1])
    else:
        print(card_list.pop(-1))
