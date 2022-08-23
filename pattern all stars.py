n=int(input("enter the number:"))
row=1
while row<=5:
    column=1
    while column<=1:
        if (column==1 or column==2):
            print("*",end="")
        else:
            print(end="")
        column+=1
    print()
    row+=1
        