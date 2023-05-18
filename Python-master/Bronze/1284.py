# 숫자별 자릿 수 개산하기
def funtion(A):
    if A == 0:
        return 4
    elif A == 1:
        return 2
    else:
        return 3
    
while True:
    N = int(input())
    sum = 0
    if N == 0:
        break
    
    if N >= 1000:
        N = list(map(int, str(N)))
        for i in range(len(N)):
            sum += funtion(N[i])  
        sum += 5
    elif N >= 100:
        N = list(map(int, str(N)))
        for i in range(len(N)):
            sum += funtion(N[i])
        sum += 4
    elif N >= 10:
        N = list(map(int, str(N)))
        for i in range(len(N)):
            sum += funtion(N[i])
        sum += 3
    else:
        sum += funtion(N)
        sum += 2
            
            
    print(sum)