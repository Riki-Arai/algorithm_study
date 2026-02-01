import sys
input = sys.stdin.readline

n, q = map(int, input().split())
nil = -1
# front[i] := 電車 i の前部に連結している電車。ないなら nil。
front = [nil] * (n + 1)
# back[i]  := 電車 i の後部に連結している電車。ないなら nil。
back = [nil] * (n + 1)

for _ in range(q):
    c, *rest = map(int, input().split())
    if c == 1:
        x, y = rest
        back[x] = y
        front[y] = x
    elif c == 2:
        x, y = rest
        back[x] = nil
        front[y] = nil
    else:  # c == 3
        x = rest[0]
        # 先頭に移動
        while front[x] != nil:
            x = front[x]
        # そこから後ろに辿る
        ans = []
        while x != nil:
            ans.append(x)
            x = back[x]
        # 出力
        print(len(ans), *ans)