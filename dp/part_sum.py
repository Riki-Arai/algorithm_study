def part_sum(A, N, W):
    if N == 0: 
        if W == 0:
            return True
        else:
            return False

    if part_sum(A, N-1, W-A[N-1]):
        return "Yes"

    if part_sum(A, N-1, W):
        return "Yes"
            
    return "No"

print(part_sum([3, 2, 6, 5], 4, 14))
