name=input("Введите имя файла\n")
count=int(input("Введите кол-во строк\n"))

f=open(name,'r')
txt_temp=f.readline()

i=1

while txt_temp!="":
    txt=""
    for j in range(count):
        txt+=txt_temp
        txt_temp=f.readline()
        if txt_temp=="":
            break
    f1=open(f"{i}.txt",'w')
    f1.write(txt)
    f1.close()
    i+=1

f.close()