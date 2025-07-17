# 塊を作ることができれば良い
N, K = map(int,input().split())
S = input()
# split
idx = [0] + [i for i in range(1,N) if S[i-1]!=S[i]] + [N]
splited_S = [S[idx[i]:idx[i+1]] for i in range(len(idx)-1)]
# swap
if S[0] == '0':
    kth_1_idx = 2*K-1
else:
    kth_1_idx = 2*K-2
splited_S[kth_1_idx-1], splited_S[kth_1_idx] = splited_S[kth_1_idx], splited_S[kth_1_idx-1]
# join
T = "".join(splited_S)
print(T)

## first
#N, K = map(int, input().split())
#S = input().strip()
#
#res_list = []
#tmp_res_list = []
#tmp_res_2_list = []
#tmp_res_3_list = []
#count = 0
#
#for ch in S:
#    if count < K - 1:
#        if len(tmp_res_list) > 0 and ch == "0":
#            count += 1
#            if count == K - 1:
#                tmp_res_list.clear()
#                tmp_res_2_list.append(ch)
#            else:
#                tmp_res_list.append(ch)
#                res_list.append(ch)
#                tmp_res_list.clear()
#        elif ch == "1":
#            res_list.append(ch)
#            tmp_res_list.append(ch)
#        else:
#            res_list.append(ch)
#
#    elif count == K - 1:
#        if len(tmp_res_list) > 0 and ch == "0":
#            count += 1
#            tmp_res_3_list = [ch]  # ここだけで上書きするので代入でOK
#        elif ch == "1":
#            tmp_res_list.append(ch)
#        else:
#            tmp_res_2_list.append(ch)
#
#    elif count == K:
#        res_list.extend(tmp_res_list)
#        res_list.extend(tmp_res_2_list)
#        res_list.extend(tmp_res_3_list)
#        res_list.append(ch)
#        count += 1
#        tmp_res_list.clear()
#        tmp_res_2_list.clear()
#        tmp_res_3_list.clear()
#
#    else:
#        res_list.append(ch)
#
#if len(tmp_res_list) > 0 and len(tmp_res_2_list) > 0:
#    print(''.join(res_list) + ''.join(tmp_res_list) + ''.join(tmp_res_2_list))
#else:
#    print(''.join(res_list))