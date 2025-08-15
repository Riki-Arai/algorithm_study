

# first
#N = int(input())
#A_lists = [list(map(int, input().split())) for _ in range(N)] # 取得例:[[1,2], [3,4]・・[9,10]]
#
#l_idx, r_idx = 0, -1
#a1, b1 = A_lists[l_idx]
#a2, b2 = A_lists[r_idx]
#sum = sum(map(lambda x: x[0], A_lists))
#tmp_sum = 0
#res = 0
#while True:
#    t = min(a1/b1, a2/b2)
#    if t == a1/b1:
#        if tmp_sum + a1 + b2*t == sum:
#            res += a1
#            break
#        elif tmp_sum + a1 + b2*t > sum:
#            if l_idx - r_idx == N:
#                a1, b1 = A_lists[l_idx]
#                res += (sum-tmp_sum)/2
#            else:
#                l_idx += 1
#                a1, b1 = A_lists[l_idx]
#                res += (sum-tmp_sum)/2
#            break
#
#        tmp_sum += a1 + b2*t
#        res += a1
#        a2 -= b2*t
#        l_idx += 1
#        a1, b1 = A_lists[l_idx]
#    elif t == a2/b2:
#        if tmp_sum + b1*t + a2 == sum:
#            res += a2
#            break
#        elif tmp_sum + b1*t + a2 > sum:
#            if tmp_sum + b1*t + a2 == sum:
#                a2, b2 = A_lists[r_idx]
#                res += (sum-tmp_sum)/2
#                break
#            elif tmp_sum + b1*t + a2 > sum:
#                r_idx -= 1
#                a2, b2 = A_lists[r_idx]
#                res += (sum-tmp_sum)/2
#                break
#
#        tmp_sum += b1*t + a2
#        res += b1*t
#        a1 -= b1*t
#        r_idx -= 1
#        a2, b2 = A_lists[r_idx]
#    else:
#        if tmp_sum + a1 + a2 == sum:
#            res += a1
#            break
#        elif tmp_sum + a1 + a2 > sum:
#            if tmp_sum + a1 + a2 == sum:
#                a2, b2 = A_lists[r_idx]
#                res += (sum-tmp_sum)/2
#                break
#            elif tmp_sum + a1 + a2 > sum:
#                l_idx += 1
#                r_idx -= 1
#                a1, b1 = A_lists[l_idx]
#                a2, b2 = A_lists[r_idx]
#                res += (sum-tmp_sum)/2
#                break
#
#        tmp_sum += a1 + a2
#        res += a1
#        l_idx += 1
#        a1, b1 = A_lists[l_idx]
#        r_idx -= 1
#        a2, b2 = A_lists[r_idx]
#
#print(res)