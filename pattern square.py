n=int(input("enter the number:"))
row=1
while row<=n:
    column=1
    while column<=n: 
        if (row==1 or  row==5 or column==1 or column==5):
            print("*",end=" ")
        else:
            print(end=" ")
        column=column+1
    print()
    row=row+1