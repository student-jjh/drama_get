import os,codecs
f=open('first.txt','w')
f.write("아 공부하기 싫다. 내일부터는 시험기간이네.")
f.close()
f=open("first.txt",'a')
f.write("시험기간은 항상 별루안거 같다는 생각이 드네.")
f.close()
f=open('first.txt','r')
print(f.read())
f.seek(0)
print(f.read())
print(f.read())
f.close()

print(os.getcwd())