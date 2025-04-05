N = int(input())

def solve(i):
    if i == 0:
        return 1
    return i * solve(i-1)

print(solve(N))