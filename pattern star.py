n=int(input("enter the number:"))
for row in range(n):
    for column in range(n):
        if column==0 or row==(n-1) or column==row:
            print("*",end="")
        else:
            print(end=" ")
    print()
    
    
