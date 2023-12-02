#Line Eliminator

#Opens Text File
File=open('FILE.txt')
MyText=File.read()
MyText.close()
MyText=MyText.splitlines()
MyTextNew=[]

for i in MyText:
    if len(i)>0:
        MyTextNew.append(i)

MyTextNew2='\n'.join(MyTextNew)

FileNew=open('FILE.txt', 'w')
FileNew.write(MyTextNew2)
FileNew.close()