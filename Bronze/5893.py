N = int(input())
N = int(str(N), 2) #2진수 -> 10진수 변환
N *= 17
N = bin(N) #10진수 -> 2진수 변환

print(int(N[2:]))