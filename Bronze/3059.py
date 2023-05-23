number = int(input())
for i in range(number):
    sum = 2015
    N = input(); N = ''.join(set(N)) # 중복된 문자 삭제
    for j in range(len(N)):
       sum -= ord(N[j])
    
    print(sum)