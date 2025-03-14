X_list = list(input())
dec_list = X_list[X_list.index(".")+1:]
dec_list.reverse()
c = 0
for x in dec_list:
    if x != "0":
        break
    c += 1

res = "".join(X_list[:X_list.index(".")+1] + list(reversed(dec_list[c:])))
if res[-1] == ".":
    print(res[:-1])
else:
    print(res)

