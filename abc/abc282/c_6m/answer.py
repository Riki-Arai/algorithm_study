N = int(input())
S_list = list(input())

flag = False
count = 0
for i, s in enumerate(S_list):
    if s == '"' and count % 2 == 0:
        flag = True
        count += 1
    elif s == '"' and count % 2 == 1:
        flag = False
        count += 1
    elif s == "," and flag == False:
        S_list[i] = "."

print("".join(S_list))