S = list(map(int, input().split()))
T = list(map(int, input().split()))
S_total = 0
T_total = 0

for i in range(4):
    S_total += S[i]
    T_total += T[i]
    
if S_total >= T_total:
    print(S_total)
else:
    print(T_total)