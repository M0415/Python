S = input()
english = [0] * 26

# ord 함수는 문자를 (아스키코드)숫자로 변환해준다
for i in S:
    #아스키코드 97이 소문자a이다
    english[ord(i) - 97] += 1
    
for j in english:
    print(j, end=" ")