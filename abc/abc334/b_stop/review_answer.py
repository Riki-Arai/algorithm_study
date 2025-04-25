A, M, L, R = map(int, input().split())

#L -= A
#R -= A
#L += 2 * 10**18
#R += 2 * 10**18
print(R//M - (L-1)//M) # 特定の範囲内に倍数が何個含むかといった時に使用する計算