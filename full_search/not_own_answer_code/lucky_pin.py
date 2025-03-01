N = int(input())
S = input()

# 1文字で作れる「数字」の集合
dp1 = set()
# 2文字で作れる「数字ペア」の集合
dp2 = set()
# 3文字で作れる「数字トリプル」の集合
dp3 = set()

for ch in S:
    # すでにあるペアそれぞれに ch を付けて 3文字の組み合わせとして追加
    for p in dp2:
        dp3.add(p + ch)
    # すでにある 1文字に ch を付けて 2文字の組み合わせとして追加
    for d in dp1:
        dp2.add(d + ch)
    # ch 自体を 1文字の集合に追加
    dp1.add(ch)

print(dp1)
print(dp2)
print(dp3)
print(len(dp3))
