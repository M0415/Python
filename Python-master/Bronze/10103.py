round = int(input())
s_1, s_2 = 100, 100


for i in range(round):
    A, B = map(int, input().split())
    if A > B:
        s_2 -= A
    elif B > A:
        s_1 -= B
        
print(s_1)
print(s_2)