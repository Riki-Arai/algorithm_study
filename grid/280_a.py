H, W = list(map(int, input().split()))

print(sum([input().count("#") for _ in range(H)]))
