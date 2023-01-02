import sys
for k in range(3):
    N = int(sys.stdin.readline())
    sum = 0
    
    for i in range(N):
        j = int(sys.stdin.readline())
        sum += j
        
    if sum == 0:
        print(0)
    elif sum > 0:
        print("+")
    else:
        print("-")