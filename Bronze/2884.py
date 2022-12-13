H, M = input().split()
H = int(H)
M = int(M)

if (M - 45) < 0 and 0 <= (H-1) <=23 :
    M = (M-45) + 60
    H = H-1
    print(H, M)
    
elif (M - 45) < 0 and (0 > (H - 1) or (H-1) > 23) :
    M = (M-45) +60
    H = H +23
    print(H,M)
    
elif (M -45) >= 0:
    M = M - 45 
    print(H,M) 