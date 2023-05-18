A, B = map(int, input().split())
C, D = map(int, input().split())
first, second = 0, 0

while A != 0 or D != 0:
    if A > 0:
        A -= 1
        first += 1
        
    if D > 0:
        D -= 1
        first += 1
        
while B != 0 or C != 0:
    if B > 0:
        B -= 1
        second += 1
        
    if C > 0:
        C -= 1
        second += 1
        
if first >= second:
    print(second)
else:
    print(first)
        