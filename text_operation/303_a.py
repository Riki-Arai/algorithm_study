N = int(input())
S = list(input())
T = list(input())

def solve():
    if S == T:
        return "Yes"
    for s, t in zip(S, T):
        if (s == "1" and t == "l") or (s == "l" and t == "1"):
            return "Yes"
        if (s == "0" and t == "o") or (s == "o" and t == "0"):
            return "Yes"
    return "No"
print(solve())
