str = str(input("Input a word : "));
word_list = list(str);
print(word_list);
result = [];
for _ in word_list:
    print(word_list);

for _ in range(len(word_list)):
    result.append(word_list.pop());

print(result);