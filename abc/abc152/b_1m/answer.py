A, B = input().split() # 取得例：A B

res_list = [A*int(B), B*int(A)]
res_list.sort()
print(res_list[0])