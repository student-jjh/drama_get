import os, re

f=open("1화대본.txt",'r')
sentence=f.readlines()

lines=[i for i in sentence if re.match(r'[A-Z][a-z]+:',i)]
print(lines[:10])

f.close()