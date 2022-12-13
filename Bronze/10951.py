while True:
    #try = except 에러가 발생할 수 있는 문장에 try를 사용하고 except문에는 에러 발생시 실행시킬 문장을 쓴다.
    try:
        A,B = map(int, input().split())
    except:
        break
    sum = 0
    sum = A+B
    print(sum)