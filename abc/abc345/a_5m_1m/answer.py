S_list = list(input())

if S_list[0] == "<" and list(set(S_list[1:-1])) == ["="] and S_list[-1] == ">":
    print("Yes")
else:
    print("No")