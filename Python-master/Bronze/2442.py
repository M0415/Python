N = int(input())

for i in range(1, N+1):
    for j in range(i, N):
        print(" ",end="")
    for k in range(0 , i + i-1):
        print("*",end="")
    print("")