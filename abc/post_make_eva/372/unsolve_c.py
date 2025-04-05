N, Q = list(map(int, input().split()))
S = input()

s_list = list(S)
res = S.count("ABC")
for _ in range(Q):
    x, c = list(map(int, input().split()))
    x -= 1
    if s_list[x] != c:
        if c == "A":
            if "".join(s_list[x+1:x+2]) == "BC"
                res += 1
            elif "".join(s_list[x-3:x]) == "ABC"
                res -= 1
            if x + 1 != len(s_list):
                elif s_list[x-1] = "A" and s_list[x] == "B" and s_list[x+1] == "C"
                    res -= 1
            s_list[x] = c
        elif c == "B":
            if x + 1 != len(s_list):
                if s_list[x-1] = "A" and s_list[x+1] == "C":
                    res += 1
            elif "".join(s_list[x-3:x]) == "ABC"
                res -= 1
            if x + 1 != len(s_list):
                elif s_list[x-1] = "A" s_list[x] == "B" and s_list[x+1] == "C"
                    res -= 1
            s_list[x] = c
        elif c == "C":
            if "".join(s_list[x+1:x+2]) == "BC"
                res += 1
            elif "".join(s_list[x-3:x]) == "ABC"
                res -= 1
            elif s_list[x-1] = "A" s_list[x] == "B" and s_list[x+1] == "C"
                res -= 1
            s_list[x] = c
        else:

