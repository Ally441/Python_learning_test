Author = 'Liu Lei'
with open("c.txt",'r',encoding="utf-8") as file ,\
        open("b.txt",'w',encoding="utf-8") as file1:
    for line in file:
        print(line)
    file1.writelines("helloworld\n")