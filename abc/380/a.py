S = input()

def solve():
    #if len(S) != 6:
    #    return "No"
    if S.count("1") != 1:
        return "No"
    if S.count("2") != 2:
        return "No"
    if S.count("3") != 3:
        return "No"
    return "Yes"

print(solve())
