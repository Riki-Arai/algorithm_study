S = input()
s_list = S.split("|")
s_list = [item for item in s_list if item != ""]

a_list = []
for s in s_list:
    a_list.append(str(len(s)))

print(*a_list)
