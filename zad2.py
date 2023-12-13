name=input("Введите имя файла\n")

f=open(name,'r')

txt=""
txt_temp=f.readline()
i=0

while txt_temp!="":
    txt+=f"{str(i+1)}.{txt_temp}"
    i+=1
    txt_temp=f.readline()
f.close()

f=open(name,'w')
f.write(txt)
f.close()
