N, R = map(int, input().split())
L = list(map(int, input().split()))

opens = [i for i, x in enumerate(L, start=1) if x == 0]

if not opens:
    print(0)
else:
    left = min(R, opens[0])          # 行く必要がある一番左の部屋
    right = max(R, opens[-1] - 1)    # 行く必要がある一番右の部屋

    closed_to_cross = 0
    for door in range(left, right):
        if L[door] == 1:
            closed_to_cross += 1

    ans = len(opens) + 2 * closed_to_cross
    print(ans)