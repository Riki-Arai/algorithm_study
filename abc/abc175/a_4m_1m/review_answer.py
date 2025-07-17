S = input().strip() # 取得例：A

if "RRR"  == S:
    print(3)
elif "RR"  in S:
    print(2)
elif "R"  in S:
    print(1)
else:
    print(0)

## first
#res = 0
#tmp_res = 0
#for i, s in enumerate(list(S), 1):
#    if s == "R":
#        tmp_res += 1
#        if i == 3:
#            res = max(tmp_res, res)
#    else:
#        res = max(tmp_res, res)
#        tmp_res = 0
#
#print(res)