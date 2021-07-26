# 사용자가 입력한 십진수를 이진수로 변환해서 출력해주는 프로그램

print("십진수 아무거나 입력하세요 : ");
decimal = int(input());
binary = '';

while(decimal > 0):
    remainder = decimal % 2; #나머지는 remainder 변수에 따로 저장
    binary = str(remainder) + binary;   #binary 문자열에 2로 나눈 나머지를 저장
    decimal = decimal // 2; #decimal을 2로 나눈 몫으로 업데이트
else:
    print("변환 작업 완료!!");
    print(binary);    