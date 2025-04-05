M, D = map(int, input().split())
y, m, d = map(int, input().split())

n_d = (d+1) % D
if n_d == 0:
    n_d = D

if n_d == 1:
    n_m = (m+1) % M 
    if n_m == 0:
        n_m = M

    if n_m == 1:
        y += 1
        print(y, n_m, n_d)
    else:
        print(y, n_m, n_d)
else:
    print(y, m, n_d)