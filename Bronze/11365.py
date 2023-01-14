while True:
    ob = input().split()
    
    # 리스트를 문자열로 변환
    ob = " ".join(ob)
    
    # 문자열 "END" 입력 시 종료
    if ob =="END":
        break
    
    # 문자열을 반대로 바꾸기
    ob_back = "".join(reversed(ob))
    print(ob_back)