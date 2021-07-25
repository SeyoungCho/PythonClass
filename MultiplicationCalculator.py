# 프로그램이 시작되면 '구구단 몇 단을 계산할까요(1~9)?' 가 출력된다.
# 사용자는 계산하고 싶은 구구단 숫자를 입력한다.
# 프로그램은 '구구단 n단을 계산합니다' 라는 메세지와 함께 구구단의 결과를 출력한다.
# 기존 문제와 달리, 이번에는 프로그램이 계속 실행되다가 종료 조건에 해당하는 숫자(여기서는 0)을 입력하면 종료된다.

dan = 1;
while True:
  
    print("구구단 몇 단을 계산할까요(1~9)? : ", end='');
    dan = int(input());
    if(dan == 0): 
        break;
    print("구구단 "+str(dan)+"단을 계산합니다.");
    for i in range (1,10):
        print(str(dan) + " * " + str(i) + " = " + str(dan*i));
    
print("구구단 계산기를 종료합니다.");
exit;
    
    