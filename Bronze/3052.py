array = []
for i in range(10):
    number = int(input())
    array.append(number % 42)

#리스트 내에서 같은 인덱스 값을 삭제하고 리스트로 정렬한다
array_set = list(set(array))
print(len(array_set))