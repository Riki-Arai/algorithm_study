S = input()
s_list = list(S)
for i in range(len(s_list)):
    if i + 1 == len(s_list):
        break

    if s_list[i] + s_list[i+1] == "WA":
        s_list[i] = "A"
        s_list[i+1] = "C"
        if i != 0 and s_list[i-1] == "W":
            s_list[i] = "C"
            s_list[i-1] = "A"

print(*s_list, sep='')
