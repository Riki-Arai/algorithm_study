s_list = list(input())
t_list = list(input())

def solve():
    if s_list == t_list:
        return "Yes"

    for i in range(len(s_list) -1):
        tmp_list = s_list.copy()
        j = s_list[i]
        k = s_list[i+1]
        tmp_list[i] = k
        tmp_list[i+1] = j
        if tmp_list == t_list:
            return "Yes"
    return "No"

print(solve())
