T = int(input())
for i in range(T):
    K = input()
    N = int(input())
    sum = 0
    for j in range(N):
        count = int(input())
        sum += count
    
    total = sum % N
    if total == 0:
        print('YES')
    else:
        print('NO')
