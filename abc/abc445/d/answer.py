import bisect as bi

N = int(input()) # 数値：1
A_list = list(map(int, input().split())) # 取得例：[1,2,3]、1行の入力用

def lis(A_list):
    n = len(A_list)
    dp_list = [float("INF")] * n
    res, tmp_res = 1, 1
    for i in range(n) :
        pos = bi.bisect_left(dp_list, A_list[i])
        if i == 0:
            dp_list[pos] = A_list[i]
        else:
            if pos == 0:
                if dp_list[pos] != float("INF") and dp_list[pos+1] != float("INF"):
                    if dp_list[pos]+1 == dp_list[pos+1]:
                        if A_list[i]+1 != dp_list[pos+1]:
                            tmp_res = max(tmp_res-1, 1)
                            res = max(tmp_res, res)
                    else:
                        if A_list[i]+1 == dp_list[pos+1]:
                            tmp_res += 1
                            res = max(tmp_res, res)
                elif dp_list[pos+1] != float("INF"):
                    if A_list[i]+1 == dp_list[pos+1]:
                        tmp_res += 1
                        res = max(tmp_res, res)
            elif pos == N-1:
                if dp_list[pos] != float("INF") and dp_list[pos-1] != float("INF"):
                    if dp_list[pos-1]+1 == dp_list[pos]:
                        if dp_list[pos-1]+1 != A_list[i]:
                            tmp_res = max(tmp_res-1, 1)
                            res = max(tmp_res, res)
                    else:
                        if dp_list[pos-1]+1 == A_list[i]:
                            tmp_res += 1
                            res = max(tmp_res, res)
                elif dp_list[pos-1] != float("INF"):
                    if dp_list[pos-1]+1 != A_list[i]:
                        tmp_res += 1
                        res = max(tmp_res, res)
            else:
                if dp_list[pos] != float("INF") and dp_list[pos+1] != float("INF"):
                    if dp_list[pos]+1 == dp_list[pos+1]:
                        if A_list[i]+1 != dp_list[pos+1]:
                            tmp_res = max(tmp_res-1, 1)
                            res = max(tmp_res, res)
                    else:
                        if A_list[i]+1 == dp_list[pos+1]:
                            tmp_res += 1
                elif dp_list[pos+1] != float("INF"):
                    if A_list[i]+1 != dp_list[pos+1]:
                        tmp_res += 1
                        res = max(tmp_res, res)

                if dp_list[pos] != float("INF") and dp_list[pos-1] != float("INF"):
                    if dp_list[pos-1]+1 == dp_list[pos]:
                        if dp_list[pos-1]+1 != A_list[i]:
                            tmp_res = max(tmp_res-1, 1)
                            res = max(tmp_res, res)
                    else:
                        if dp_list[pos-1]+1 == A_list[i]:
                            tmp_res += 1
                            res = max(tmp_res, res)
                elif dp_list[pos-1] != float("INF"):
                    if dp_list[pos-1]+1 != A_list[i]:
                        tmp_res += 1
                        res = max(tmp_res, res)
            dp_list[pos] = A_list[i]

    return res

print(lis(A_list))