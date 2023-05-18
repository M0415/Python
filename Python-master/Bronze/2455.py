li = []
total = 0
for i in range(4):
    A, B = map(int, input().split())
    total += B - A
    li.append(total)

print(max(li))