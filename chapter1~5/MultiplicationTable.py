# 프로그램이 시작되면 '구구단 몇 단을 계산할까?'가 출력된다.
# 사용자는 계산하고 싶은 구구단 숫자를 입력한다.
# 프로그램은 '구구단 n단을 계산한다.' 라는 메세지와 함께 구구단의 결과를 출력한다.

print("구구단 몇 단을 계산할까?");
dan = int(input());
if(type(dan) != int):
    print("단 입력 제대로 하세요.");
else:
    for i in range(1, 10):
        result = dan*i;
        print(dan, "*", i, "=", result);

exit;
