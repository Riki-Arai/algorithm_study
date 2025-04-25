A, M, L, R = map(int, input().split())

#L -= A
#R -= A
#L += 2 * 10**18
#R += 2 * 10**18

print(R//M - (L-1)//M)