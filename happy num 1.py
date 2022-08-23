n=int(input("enter the number:"))
temp=n
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem*rem
        temp=temp//10
    temp=sum
if sum==1:
    print(n,"happy number")
else:
    print(n,"not happy number")
    
#     6899
    
    
    
# n=int(input("enter the number:"))
# temp=n
# sum=0
# while temp>=0:
    # digit=temp%10
    # sum=sum+digit
    # temp=temp//10
# if temp==sum:
    # print("happy number")
# else:
    # print("not a happy number")