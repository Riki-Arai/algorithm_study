import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# dish_ings[i]: 料理iでまだ「未解禁」の食材集合
dish_ings = []

# ing_to_dishes[x]: 食材xを使っている料理の集合
ing_to_dishes = [set() for _ in range(N + 1)]

for i in range(M):
    row = list(map(int, input().split()))
    K = row[0]
    A = row[1:]

    s = set(A)
    dish_ings.append(s)

    for a in A:
        ing_to_dishes[a].add(i)

B = list(map(int, input().split()))

ans = 0
res = []

for b in B:
    # 食材bを使っている料理を全部見る
    for dish in ing_to_dishes[b]:
        # まだ未解禁集合に b が残っていれば消す
        if b in dish_ings[dish]:
            dish_ings[dish].remove(b)
            if len(dish_ings[dish]) == 0:
                ans += 1

    res.append(str(ans))

print("\n".join(res))