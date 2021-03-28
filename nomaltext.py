import re
example="이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재형, 2019). 또다른 견해도 있었습니다(Lion, 2018)"
result=re.findall(r'\([A-Za-z가-힣]+, \d+\)',example)
print(result)

example1="저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다."
find=re.findall(r'\d+?년',example1)
print(find)

sentence="I have a lovely dog, really. I am not telling a lie. What a pretty dog!"
sentence=re.sub(r'dog','cat',sentence)
after_split=re.split(r"[.!?]",sentence)
print(after_split)