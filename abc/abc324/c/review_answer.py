# 編集距離は扱う機会があるので今回の関数を登録しても良いかも？
N, T = input().split()
N = int(N)

def f(s, t):
    if s == t:
        return True
    # これがないことが原因でACできなかったので注意(2回やった)
    if len(s) < len(t) - 1:
        return False
    else:
        s_i, t_i, miss = 0, 0, 0
        while s_i < len(s):
            if s[s_i] == t[t_i]:
                s_i += 1
                t_i += 1
            else:
                miss += 1
                if miss >= 2:
                    return False
                # 文字列数が同じ時はお互いのidxを+1するように処理
                if len(s) == len(t):
                    s_i += 1
                t_i += 1

        return True

res_list = []
for i in range(1, N+1):
    S = input()
    if len(S) > len(T):
        if f(T, S):
            res_list.append(i)
    else:
        if f(S, T):
            res_list.append(i)

print(len(res_list))
print(*res_list)