T = int(input())

for i in range(T):
    S = input().split()
    R = int(S[0])
    result = ""
    for j in range(len(S[1])):
        mix = S[1][j] * R
        result += mix
    
    print(result)