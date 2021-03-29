import os, re, codecs
f=codecs.open("1화대본.txt",'r',encoding='utf-8')
script101=f.read()
Line = re.findall(r'Monica:.+',script101)
char=re.compile(r'[A-Z][a-z]+:')
chars=re.findall(char,script101)
chars=set(chars)
a=list(chars)
character=[]
for i in a:
    character.append(i[:-1])

print(character)
f.close()