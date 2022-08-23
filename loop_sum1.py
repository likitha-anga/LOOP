# num=int(input("enter the number:"))
# for row in range(1,5):
#     for column in range(1,5):
#         print(row==0,row==1,row==2,)
#     print()

    
n=int(input("enter the number:"))
i=1
sum=1
while i<=n:
    j=1
    while j<n:
        print(sum,end=" ")
        sum+=1
        j+=1
    print()
    i+=1
    
    