# 비틀즈 노래 yesterday 가사중 'yesterday'가 몇 번 나오는 지 
# 카운팅하는 프로그램이다. 

f = open("yesterday.txt", "r");
yesterday_lyric = f.readlines();
f.close();
count = 0;
for line in yesterday_lyric:
    count += line.strip().upper().count("YESTERDAY");
    #count += line.strip().count("Yesterday");

print("Number of a word 'yesterday' :", count);