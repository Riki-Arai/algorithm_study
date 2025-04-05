N, K = map(int, input().split())
print(sum(list(map(lambda x: x // K, list(map(lambda x: len(x), input().strip().split("X")))))))