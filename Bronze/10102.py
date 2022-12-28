T = int(input())
N = list((input().split()))
A, B = 0,0
for i in range(T):
    if N[0][i] == "A":
        A += 1
    elif N[0][i] == "B":
        B += 1
        
if A > B:
    print("A")
elif B > A:
    print("B")
elif A == B:
    print("Tie")