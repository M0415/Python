number = list(map(int, input().split()))
i = input()
number.sort()
a = []
for j in i:
    if j == 'A':
        a.append(number[0])
    elif j == 'B':
        a.append(number[1])
    elif j == 'C':
        a.append(number[2])
a = ' '.join(str(b) for b in a)
print(a)