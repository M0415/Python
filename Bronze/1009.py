import sys
N = int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    A = A%10
    
    if A == 0:
        print(10)
    elif A in [1, 5, 6]:
        print(A)
    elif A in [4, 9]:
        B_1 = B%2
        if B_1 == 0:
            print((A*A) %10)
        else:
            print(A)
    elif A in [2, 3, 7, 8]:
        B_2 = B%4
        if B_2 == 0:
            print((A**4) % 10)
        else:
            print((A**B_2) % 10)