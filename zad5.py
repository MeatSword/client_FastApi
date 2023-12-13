name=input("Введите имя файла\n")
var=input("1 - вывод первых , 2 - вывод последних\n")
count = int(input("Число строк\n"))

f=open(name,'r',encoding="utf-8")
txt_list=f.readlines()
txt=""

if var=="1":
    i=0
    while i<count:
        txt+=f"{str(i+1)}.{txt_list[i]}"
        i+=1
elif var=="2":
    i = len(txt_list)-1
    while i > len(txt_list)-count-1:
        txt += f"{str(i + 1)}.{txt_list[i]}"
        i -= 1
print(txt)