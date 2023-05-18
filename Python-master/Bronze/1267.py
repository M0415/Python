N = int(input())
M = list(map(int, input().split()))
yon, min = 0,0
    
for i in range(N):
    #영식 30초마다 10원 but 29초까지만 10원, 30초는 20원
    if (M[i] // 30) > 0:
        yon += (M[i] // 30) * 10
        if (M[i] % 30) >= 0:
            yon += 10
    elif M[i] // 30 == 0:
        yon += 10
    #민식 60초마다 15원 but 59초까지만 15원, 60초는 30원
    if (M[i] // 60) > 0:
        min += (M[i] // 60) * 15
        if (M[i] % 60) >= 0:
            min += 15
    elif M[i] // 60 == 0:
        min += 15
        
if yon == min:
    print("Y M {}".format(yon))
elif yon > min:
    print("M {}".format(min))
elif yon < min:
    print("Y {}".format(yon))