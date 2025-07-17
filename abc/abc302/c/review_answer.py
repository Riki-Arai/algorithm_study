# 解説をみれば順列探索をやるかどうかだけだったが、何気にそのような問題に取り組んだ経験は浅く、解説ACとなってしまった
import itertools

N, M = map(int, input().split())
S_list = [input() for _ in range(N)]

for ps in itertools.permutations(S_list):
    for i in range(N-1):
        # perm[i] と perm[i+1] を比べて異なる文字数を数える
        count = sum(a != b for a, b in zip(ps[i], ps[i+1]))
        if count != 1:
            break
    # breakしなかった場合にYes
    else:
        print("Yes")
        exit()

print("No")