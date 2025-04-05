S_list = list(input().strip())

if S_list.count("<") == 1 and S_list.count(">") == 1 and S_list.index("<") < S_list.index("=") and S_list.index("=") < S_list.index(">"):
    print("Yes")
else:
    print("No")