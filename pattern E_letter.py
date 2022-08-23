# n=int(input("enter the number:"))
row=1
while row<=5:
    column=1
    while column<=5:
        if (column==1 or (row==1 or row==3 or row==5)):
            print("*",end="")
        else:
            print(end="")
        column+=1
    print()
    row+=1