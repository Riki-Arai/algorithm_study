N = int(input())
A_list = list(map(int, input().split()))

res_list = []
min_a, max_a = min(A_list), max(A_list)
tmp_res_list = [max_a, min_a + max_a]
s_a_list = sorted(A_list)
def f(tmp_res):
    rem_list = sorted([a for a in A_list if a != tmp_res])
    if len(rem_list)%2 != 0:
        return False

    head_i = 0
    tail_i = len(rem_list)-1
    while head_i < tail_i:
        h = rem_list[head_i]
        t = rem_list[tail_i]
        if h+t != tmp_res:
            return False
        head_i += 1
        tail_i -= 1

    return True

res_list = []
for tmp_res in tmp_res_list:
    if f(tmp_res):
        res_list.append(tmp_res)

print(*res_list)



N = int(input())
A_list = list(map(int, input().split()))

res_list = []
tmp_res_list = [max(A_list), min(A_list) + max(A_list)]
s_a_list = sorted(A_list)

def is_ok(res):
    # 長さが res のものは「分割されていない1本」なので除外してよい
    remain_list = [a for a in s_a_list if a != res]

    # 残りは2本ずつ組になる必要がある
    if len(remain_list) % 2 == 1:
        return False

    head_i = 0
    tail_i = len(remain_list) - 1

    # 最小と最大を順に組ませる
    while head_i < tail_i:
        if remain_list[head_i] + remain_list[tail_i] != res:
            return False
        head_i += 1
        tail_i -= 1

    return True

for res in tmp_res_list:
    if res not in res_list and is_ok(res):
        res_list.append(res)

print(*res_list)