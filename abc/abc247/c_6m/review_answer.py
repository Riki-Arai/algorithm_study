N = int(input())

def f(i):
    if i == 1:
        return ["1"]

    return f(i-1) + [str(i)] + f(i-1)

print(*f(N))