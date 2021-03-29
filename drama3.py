import os, re, codecs
f=codecs.open("1화대본.txt",'r',encoding='utf-8')
script101=f.read()
Line = re.findall(r'Monica:.+',script101)
help=re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101)
print(help[:6])
f.close()