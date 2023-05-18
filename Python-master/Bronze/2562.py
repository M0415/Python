number = [int(input()) for i in range(9)]
x = 0

for j in range(9):
    if number[j] > x:
        x = number[j]

print(x)
print(number.index(x)+1)