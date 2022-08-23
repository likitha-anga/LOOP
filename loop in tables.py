# num=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i=i+1


num=int(input("enter the number:"))
i=1
while i<=num:
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j+=1
    i+=1
    print()