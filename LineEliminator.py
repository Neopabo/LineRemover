#Line Eliminator

#Opens Text File
File=open('FILE.txt')
MyText=File.read()
File.close()
MyText=MyText.splitlines()

MyTextNew=[i for i in MyText if len(i)>0]

MyTextNew2='\n'.join(MyTextNew)

FileNew=open('FILE.txt', 'w')
FileNew.write(MyTextNew2)
FileNew.close()
