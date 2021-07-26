# 사용자로부터 입력받은 문자열을 반복문을 이용해 
# 역순으로 출력하는 프로그램 
# ex) I love you 입력 ----> uoy evol uoY 출력

print("문자열 입력하세요 : ");
sentence = str(input());
reverse_sentence = '';
for i in sentence:
    reverse_sentence = i + reverse_sentence;
print(reverse_sentence);