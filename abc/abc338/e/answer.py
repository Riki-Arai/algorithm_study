N = int(input())
AB = []
for i in range(N):
    a, b = map(int,input().split())
    AB.append((a, i))
    AB.append((b, i))

# 左端から順番にはじまることになる
AB = sorted(AB)
stack = [AB[0]]
for k in range(1, 2*N):
    v, c = AB[k]
    # stackに直前にappendしたcと現在見ているcが一致していれば、交差していないことががわかる
    # これがずっと続けばstackは空になるはず
    if stack and stack[-1][1] == c:
        stack.pop()
    # 番号が異なる場合は交差をしていることが確定
    else:
        stack.append((v, c))
if stack:
    print("Yes")
else:
    print("No")