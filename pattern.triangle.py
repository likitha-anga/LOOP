num=int(input("enter the number:"))
row=1
while row<=num:
    column=1
    while column<=num:
        if row==5 or column==(num-4) or row==column:
            print("*",end="")
        else:
            print(end=" ")
        column+=1
    print()
    row+=1


#   harsad number:
# num=int(input("enter the number:"))
# i=1
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum=sum+digit
#     temp=temp//10
# if num%sum==0:
#     print("harshad number")
# else:
#     print("not a harshad number")




# 54321
# 5432
# 543
# 54
# 5   

n=int(input("enter the number:"))
i=1
while i<=n:
    j=1
    while i<=i:
        print(j,end="") 
        j+=1
    print()
    i+=1
    
