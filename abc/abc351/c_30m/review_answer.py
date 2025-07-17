# 乗数は場合によっては極端に計算が遅くなるのでなるべく利用しない
# while文のように後戻りがあるものの、計算量としては実はそこまで重くならない
# 順列のような処理ではない限りはあまり計算量を気にしなくても良いかも
N = int(input())
A_list = list(map(int, input().split()))

res_list = []
for a in A_list:
    tmp_a = a
    while len(res_list) > 0 and res_list[-1] == tmp_a:
        tmp_a = res_list.pop(-1) + 1
    res_list.append(tmp_a)

print(len(res_list))