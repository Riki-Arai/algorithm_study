A, B, C, D, E, F, X = map(int, input().split())

x, y = divmod(X, A+C)
y = min(y, A)
t_time = A*B*x + y*B

x, y = divmod(X, D+F)
y = min(y, D)
a_time = D*E*x + y*E

if a_time > t_time:
    print("Aoki")
elif a_time == t_time:
    print("Draw")
else:
    print("Takahashi")