n = int(input('단을 입력하세요 : '));
for i in range(n):
    print('{0:>{1}s}'.format("*"*(2*i + 1), i+n));
