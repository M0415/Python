p = int(input())
A = [0] * p
result = 0

for i in range(p):
    o = list(map(int, input().split()))
    
    #세 수가 모두 같을 때
    if o[0] == o[1] and o[1] == o[2]:
        A[i] = 10000 + (o[0] * 1000)
        
    #세 수중 2수만 같을 때
    elif o[0] == o[1] or o[0] == o[2] or o[1] == o[2]:
        if o[0] == o[1]:
            A[i] = 1000 + (o[0] * 100)
        elif o[1] == o[2]:
            A[i] = 1000 + (o[1] * 100)
        elif o[0] == o[2]:
            A[i] = 1000 + (o[0] * 100)
            
    #세 수가 모두 다를떄
    else:
        if o[0] > o[1] and o[0] > o[2]:
            A[i] = o[0] * 100
        elif o[1] > o[0] and o[1] > o[2]:
            A[i] = o[1] * 100
        elif o[2] > o[0] and o[2] > o[1]:
            A[i] = o[2] * 100


for j in range(p):
    if A[j] >= result:
        result = A[j]

print(result)