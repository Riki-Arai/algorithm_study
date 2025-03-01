N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))

def need_score():
    for k in range(K+1):
        score_list = A.copy() 
        score_list.append(k)
        if (sum(score_list) / len(score_list)) >= M:
            return k

    return -1

print(need_score())
