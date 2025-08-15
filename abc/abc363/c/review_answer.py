import math, itertools, more_itertools, bisect, functools, copy
from collections import defaultdict, Counter, deque
from decimal import Decimal, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN


N, K = map(int, input().split())
S = input().strip()

p_s_list = [''.join(i) for i in  more_itertools.distinct_permutations(S)]

res = 0
for perm in p_s_list:
    has_no_palindrome = True
    # iはすでに0-baseとして扱われており、むしろ+1しないとN-Kを含んでくれない
    for i in range(N - K + 1):
        # 長さKの部分文字列 perm[i..i+K-1] が回文かどうかチェック
        is_palindrome = True
        # 一方でjは1-baseとして扱われているのでrange(K)
        for j in range(K):
            # jのみが1-baseなのでi+K+1-(j+1)-1=i + K - 1 - j
            if perm[i + j] != perm[i + K - 1 - j]:
                is_palindrome = False
                break
        if is_palindrome:
            # 一つでも回文部分文字列があればフラグを折ってループを抜ける
            has_no_palindrome = False
            break

    if has_no_palindrome:
        res += 1

print(res)