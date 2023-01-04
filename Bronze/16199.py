year, mon, day = map(int, input().split())
A, B, C = map(int, input().split())

if mon < B:
    x = A - year
elif B == mon:
    if C >= day:
        x = A - year
    else:
        x = A -year - 1
elif B < mon:
        x = A - year - 1
    
y = A - year + 1
z = A - year
        
print(x)
print(y)
print(z)
