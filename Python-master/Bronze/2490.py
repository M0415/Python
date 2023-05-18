li = {3:'A', 2:'B', 1:'C', 0:'D', 4:'E'}
for j in range(3):
    select = list(map(int, input().split()))
    sum = 0
    for i in range(4):
        sum += select[i]
    print(li[sum])