while True:
    a, b, c = input().split()
    b = int(b)
    c = int(c)
    if b > 17 or c >= 80:
        d = "Senior"
    elif b <17 or c <= 80:
        d = "Junior"
    if a == "#" and b == 0 and c == 0:
        break
    print(a, d)