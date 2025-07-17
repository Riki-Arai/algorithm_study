s_list = list(input())
i = 0

while i + 1 < len(s_list):
    if s_list[i] == "W" and s_list[i + 1] == "A":
        s_list[i] = "A"
        s_list[i + 1] = "C"
        i = max(0, i - 1)
    else:
        i += 1

print(''.join(s_list))