S = input()
T = input()

def solve():
    for i in range(len(S)):
        if S[i] != T[i]:
            return i + 1
    return len(T)

print(solve())
