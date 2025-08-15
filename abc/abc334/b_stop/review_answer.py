# 解答は一例しか示していないっぽく、実際には場合分けが必要だった
A, M, L, R = map(int, input().split())

L -= A
R -= A
if L > 0:
    print(abs(R//M-(L-1)//M))
elif L < 0:
    R *= -1
    L *= -1
    print(abs(L//M-(R-1)//M))
else:
    print(abs(L//M)+abs(R//M))