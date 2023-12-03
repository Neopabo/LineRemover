#Line Eliminator

File=open('FILE.txt') #Original Text File
MyText=File.read()
File.close()
MyText=MyText.splitlines()
MyTextNew=[]

for i in MyText:
    if len(i)>0:
        MyTextNew.append(i)

MyTextNew2='\n'.join(MyTextNew)

FileNew=open('FILE.txt', 'w') #New Text File
FileNew.write(MyTextNew2)
FileNew.close()
