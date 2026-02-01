S = input().strip() # 取得例："A"

m_i = (len(S)+1)//2
print(S[:m_i-1] + S[m_i:])