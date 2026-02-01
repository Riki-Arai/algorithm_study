S = input().strip() # 取得例："A"

alp_set = set(list(S))
alp_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for x in alp_list:
    if x not in alp_set:
        print(x)
        exit()