N, D = list(map(int, input().split()))
S = input()

print(len(S) -(S.count("@") - D))
