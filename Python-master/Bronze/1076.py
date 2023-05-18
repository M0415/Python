resist = ['black', 'brown', 'red', 'orange','yellow',\
    'green', 'blue', 'violet', 'grey','white']

# resist 몇번째 인덱스인지
A = resist.index(input())
B = resist.index(input())
C = resist.index(input())

result = str(A)
result += str(B)
result = int(result) * (10 ** C)
print(result) 