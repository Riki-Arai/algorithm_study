a, b, c = map(int, input().split()) # 取得例：1 2

if len(set([a, b, c])) in (1, 2):
    print("Yes")
else:
    print("No")