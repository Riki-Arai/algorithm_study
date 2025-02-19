S = input()

count, max_count = 0, 0
for s in S:
    if s in ["A", "C", "G", "T"]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0

if count > max_count:
    max_count = count
print(max_count)
