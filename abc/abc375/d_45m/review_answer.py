s = input().strip()
n = len(s)

lcnt = [0] * 26
rcnt = [0] * 26

# 右側カウントの初期化
for ch in s:
    rcnt[ord(ch) - ord('A')] += 1

ans = 0

for j in range(n):
    idx = ord(s[j]) - ord('A')
    # 今の文字を右側から除く
    rcnt[idx] -= 1
    # 全ての文字について積を加算
    for c in range(26):
        ans += lcnt[c] * rcnt[c]
    # 今の文字を左側に追加
    lcnt[idx] += 1

print(ans)