names = [str(name+".txt") for name in input("Введите имена файлов\n").split(',')]
txt=""

for i in range(len(names)):
    f=open(names[i],'r')

    txt_temp=f.readline().rstrip()
    while txt_temp!="":
        txt+=txt_temp+"\n"
        txt_temp=f.readline().rstrip()
    f.close()
    txt+=f"Имя файла = {names[i]}\n\n"
f=open("Выход.txt",'w')
f.write(txt)
f.close()
