a, b, w = map(int, input().split())
w *= 1000

mi = w//b
ma = w//a

if w%b != 0:
    mi += 1

if mi > ma:
    print("UNSATISFIABLE")
else:
    print(mi, ma)