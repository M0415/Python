N = int(input())

for i in range(0, N):
    for k in range(N - i, N):
        print(" ", end="")
    for j in range(0, N - i):
        print("*", end="")
    print("")