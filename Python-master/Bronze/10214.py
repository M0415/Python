T = int(input())

for i in range(T):
    yon, kon = 0,0
    for j in range(9):
        A, B = map(int, input().split())
        yon += A
        kon += B
    
    if yon > kon:
        print("Yonsei")
    elif kon > yon:
        print("Korea")
    elif yon == kon:
        print("Draw")