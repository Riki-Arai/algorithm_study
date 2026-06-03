import sys; sys.setrecursionlimit(10**7)

N = int(input()) # 数値：1

def f(X):
    x_list = []
    for x in X:
        if len(x_list):
            if x == ")":
                if x_list[-1] == "(xx":
                    x_list.pop()
                    if len(x_list):
                        x_list[-1] += "xx"
                    else:
                        x_list.append("xx")
                else:
                    x_list[-1] += x
            elif x == "(":
                x_list.append(x)
            else:
                x_list[-1] += x
        else:
            x_list.append(x)

    return "".join(x_list)

for _ in range(N):
    A = input().strip() # 取得例："A"
    B = input().strip() # 取得例："A"

    a = f(A)
    b = f(B)
    if a == b:
        print("Yes")
    else:
        print("No")