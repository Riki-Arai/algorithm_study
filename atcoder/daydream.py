'''
メモ
・dream erase(+r)の並びでdreamerで削除
・erase erase(+r)の並びでeraserで削除
・dreamer dreamなどでdreamで削除
・eraser eraceなどでeraseで削除
'''

S = input()
T = ["dream", "dreamer", "erase", "eraser"]

count = 4
while count > 0:
    for t in T:
        if t == S:
            S = ""
            count = 0
            break

        if S.startswith(t):
            d_S = S[len(t):]
            for i, t in enumerate(T, 1):
                if d_S.startswith(t):
                    S = d_S
                    count = 4
                    break
                elif i == 4:
                    count -= 1
        else:
            count -= 1

if len(S) == 0:
    print("YES")
else:
    print("NO")
