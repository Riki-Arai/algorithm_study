H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# (1) 何も置かない時の XOR
total_xor = 0
for i in range(H):
    for j in range(W):
        total_xor ^= A[i][j]

# (2) 縦・横のドミノ候補を愚直に列挙
vertical = []
horizontal = []

for i in range(H - 1):
    for j in range(W):
        vertical.append(((i, j), (i + 1, j)))

for i in range(H):
    for j in range(W - 1):
        horizontal.append(((i, j), (i, j + 1)))

# (3)(4) bit探索で、同じマスに置かないパターンだけ取得
def enumerate_patterns(dominoes):
    patterns = []
    n = len(dominoes)

    for bit in range(1 << n):
        used = set()
        xor_val = 0
        ok = True

        for k in range(n):
            if not ((bit >> k) & 1):
                continue

            c1, c2 = dominoes[k]

            if c1 in used or c2 in used:
                ok = False
                break

            used.add(c1)
            used.add(c2)

            xor_val ^= A[c1[0]][c1[1]]
            xor_val ^= A[c2[0]][c2[1]]

        if ok:
            patterns.append((used, xor_val))

    return patterns

vertical_patterns = enumerate_patterns(vertical)
horizontal_patterns = enumerate_patterns(horizontal)

# (5) 置いたマスの XOR を total_xor に適用して最大値を更新
ans = total_xor

for v_used, v_xor in vertical_patterns:
    for h_used, h_xor in horizontal_patterns:
        if v_used & h_used:
            continue

        score = total_xor ^ v_xor ^ h_xor
        ans = max(ans, score)

print(ans)