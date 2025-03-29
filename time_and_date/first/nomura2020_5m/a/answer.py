H_1, M_1, H_2, M_2, K = map(int, input().split())
diff_time = (H_2*60+M_2) - (H_1*60+M_1)
print(diff_time-K)