A, B, C, D, E, F, X = map(int, input().split())

x, y = divmod(X, A+C)
if y >= A:
    t_dis = x*A*B + A*B
else:
    t_dis = x*A*B + y*B

x, y = divmod(X, D+F)
if y >= D:
    a_dis = x*D*E + D*E
else:
    a_dis = x*D*E + y*E

if a_dis > t_dis:
    print("Aoki")
elif a_dis < t_dis:
    print("Takahashi")
else:
    print("Draw")