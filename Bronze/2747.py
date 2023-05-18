# 시간초과 1초를 대입하지 않았을 때 
# N = int(input())

# fiboo = {1 : 1, 2 : 1}

# def fibo(n):
    
#     if n <= 2:
#         return fiboo[n]
#     else:
#         return fibo(n-1) + fibo(n-2)


# fi = fibo(N)  
# fiboo[N] = fi
# print(fi)

# 시간초과 1초를 대입하였을 때 
N = int(input())

fibo = [0] * 46
fibo[1] = 1

for i in range(2, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
print(fibo[N])