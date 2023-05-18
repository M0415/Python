T = int(input())

for i in range(T):
    result = 0
    ct = input().split()
    # @ = 3곱하기 % = 5더하기 # 7빼기
    ct[0] = float(ct[0])
    result += ct[0]
    for j in range(1, len(ct)):
       if ct[j] == "@":
           result *= 3
       elif ct[j] == "%":
           result += 5
       elif ct[j] == "#":
           result -= 7
    
    print("{:.2f}".format(result)) 
