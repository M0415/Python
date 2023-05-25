num = list(map(int, input().split()))
num.sort()
if (num[1] - num[0]) == (num[2] - num[1]):
    result = num[1] - num[0]
    result = num[2] + result
else:
    if (num[1] - num[0]) > (num[2] - num[1]):
        result = (num[2] - num[1])
        result = num[1] - result
    else:
        result = (num[1] - num[0])
        result = num[1] + result
print(result)