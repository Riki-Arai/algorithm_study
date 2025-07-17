## 平面操作と呼ばれるものらしい？？
## 自分よりも右下に点がないようにすることがポイント
import sys
input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    a, c = map(int, input().split())
    cards.append((a, c, i))

#　コストが低い順にソートし、少なくともコストが一番低いものは後の処理で答えとして追加できるようにする
cards.sort(key=lambda x: x[1])
ans = []
v = 0 # 最初の攻撃力の閾値は0
for a, c, index in cards:
    # 自分よりもコストが低いものの攻撃力と自分の攻撃力を比較
    # 上回っていれば攻撃力の閾値を更新。下回っていれば自分が右下にあることになるので答えに追加しない。
    if a > v:
        v = a
        ans.append(index)

ans.sort()

print(len(ans))
print(' '.join(str(x + 1) for x in ans))