#사용자로부터 인풋이 들어온다.

word1 = input("끝말잇기를 시작합시다 : ") #인풋의 값은 기본적으로 string


if (len(word1) == 3):
    #계속 진행
        
    while True:
        word2 = input()
        
        if (len(word2) == 3) and (word2[0]) == (word1[-1]):
            print("정답입니다.") #계속진행
            
        else:
            print("오답입니다")
            
            break
else:
    print("오답입니다.")
    #종료

print("게임이 끝났습니다.")

#그 인풋을 받아서 끝자리 음절과
#다음 인풋의 첫음절이 같아야 통과다.

#3글자만 허용


#깃 변경사항 체크용
test test test
