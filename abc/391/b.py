N = int(input())
A = list(map(int, input().split()))

def hoge():
    tmp = A[1] / A[0]
    for i in range(N-1):
        if  A[i+1] / A[i] != tmp:
            return "No"

    return "Yes"

print(hoge())
