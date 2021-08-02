# 문장의 단어 개수를 파악하는 코드를 작성한다.
# defaultdict 모듈을 사용한다. 
# 단어의 출현 횟수를 기준으로 정렬된 결과를 보여주기 위하여 OrderedDict모듈을 사용한다. 

from collections import defaultdict, OrderedDict
from typing import Counter;

text = """A press release is the quickest and easiest way to get free 
publicity. If well written, a press release can result in multiple 
published articles about your firm and its products. 
And that can mean new prospects contacting you asking 
you to sell to them.""".lower().split();

def sort_by_key(t):
    return t[0];
    
d = defaultdict(lambda:0);
d = text;
c = Counter(d);
for k,v in OrderedDict(sorted(d.items(), key=sort_by_key)).items():
    print(k, v);