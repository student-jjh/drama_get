import os, re, codecs
f=codecs.open("1화대본.txt",'r',encoding='utf-8')
script101=f.read()
Line = re.findall(r'Monica:.+',script101)
monica=''
for i in Line:
    monica += (i+'\n')
f.close()
f=open('monica.txt','w',encoding='utf-8')
f.write(monica)
f.close()