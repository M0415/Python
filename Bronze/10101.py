import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

if A == B and A == C:
    print("Equilateral")
elif (A+B+C) == 180 and (A == B or A == C or B == C):
    print("Isosceles")
elif (A+B+C) == 180 and A != B and A != C and B != C:
    print("Scalene")
else:
    print("Error")