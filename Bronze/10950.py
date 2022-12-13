T = int(input())

# range(T)로 5값이 들어갈 때 {5번 반복}
for i in range(T):
    A, B = map(int, input().split())
    print(A+B)