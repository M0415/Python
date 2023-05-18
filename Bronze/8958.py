N = int(input())

for i in range(N):
    count = 0
    total = 0
    test = input()
    test = list(''.join(test))
    for j in range(len(test)):
        if test[j] == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)