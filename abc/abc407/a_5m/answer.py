A, B = map(int, input().split()) # 取得例：1 2

if A%B == 0:
    print(A//B)
    exit()

res1 = A//B
res2 = (A+B-1)//B
if abs(A/B-res1) < abs(A/B-res2):
    print(res1)
elif abs(A/B-res1) > abs(A/B-res2):
    print(res2)