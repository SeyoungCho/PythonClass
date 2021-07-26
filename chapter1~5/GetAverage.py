# 이차원 리스트리므로 각 행을 호출하고 각 열에 있는 값을 더해 학생별 평균을 구한다. 
# for문 2개를 사용한다. 

kor_score = [49, 80, 20, 100, 80];
mat_score = [43, 60, 85, 30, 90];
eng_score = [49, 82, 48, 50, 100];

midterm_score = [kor_score, mat_score, eng_score];
avg = [0, 0, 0, 0, 0];
i = 0;
for subject in midterm_score:
    for score in subject:
        avg[i] += score;
        i += 1;
    i = 0;
else:
    a, b, c, d, e = avg;
    avg = [a/3, b/3, c/3, d/3, e/3];
    print(avg);
exit;
        