A, B = map(int, input().split())
C = int(input())

A += int((B+C) / 60)
B = (B+C) % 60

if A >= 24 :
    A += -24

print(A, B)