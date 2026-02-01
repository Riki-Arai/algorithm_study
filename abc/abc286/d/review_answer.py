import sys
input = sys.stdin.readline

N, X = map(int, input().split())
coin_list = [tuple(map(int, input().split())) for _ in range(N)]

dp_list = [False]*(X+1)
dp_list[0] = True  # 0円は何も使わずに作れる

for a, b in coin_list:
    # 金額を大きいほうから順に見ることで、同じ種類のコインを
    # 重複して使わないようにする
    for current in range(X, -1, -1):
        if dp_list[current]:
            for use_num in range(1, b+1):
                nxt = current + a*use_num
                if nxt > X:
                    break
                dp_list[nxt] = True

if dp_list[X]:
    print("Yes")
else:
    print("No")