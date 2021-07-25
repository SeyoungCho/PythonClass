# 숫자찾기 게임
# 1~100의 범위에 있는 랜덤 정수를 찾아라.
# 사용자가 추측한 답을 제시하면 up, down으로 알려준다. 
# 8번 안에 못찾으면 Computer Win, 8번 내로 찾으면 You Win!
import random;

answer = random.randint(1,100);
trial = 1;
print("Guess a number between 1 ~ 100 : ", end='');
guess = int(input());

while True:
    trial += 1;
    if trial != 0:
        print(str(trial) + "th trial", end=' ');
        guess = int(input("Guess again : "));
    if guess == answer :
        print("You win! the answer is : ", answer);
        break;
    elif trial > 8 :
        print("You didn't get it in 8 trials! You lose! The answer is : ", answer);
        break;
    elif answer > guess:
        print("UP");
    elif answer < guess:
        print("DOWN");
    else: 
        trial -= 1;
        print("Wrong input. Try again.");


        