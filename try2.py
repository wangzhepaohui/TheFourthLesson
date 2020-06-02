#对文件操作
todo = open('a.txt','a')
print('1 2 3',file=todo)
print('4 5 6',file=todo)
print('7 8 9',file=todo)
todo.close()

tasks = open('a.txt')
for item in tasks:
    print(item,end="")
tasks.close()

doc = open('test.txt','w+')
print('file name:',doc.name)
doc.write('测试文件！\nwelcome')
context = doc.read()
print('内容',context)
doc.close()

doc = open('test.txt','r')
context = doc.read()
print('内容',context)
doc.close()

#指针操作
import os
doc = open('test.txt','w+')
print('file name:',doc.name)
doc.write('测试文件！\nwelcome')
print(doc.tell())
doc.seek(os.SEEK_SET)
context = doc.read()
print('内容',context)
doc.close()

#自动关闭文件，能避免忘记关闭导致的错误
with open('test.txt')as task:
    for item in task:
        print(item,end="")
