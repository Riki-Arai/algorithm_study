N = int(input()) # 数値：1

if N%2 == 0:
    n = (N-2)//2
    print("-"*n + "==" + "-"*n)
else:
    n = (N-1)//2
    print("-"*n + "=" + "-"*n)