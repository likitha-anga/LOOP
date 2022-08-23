num=int(input("enter the number:"))
temp=num
while sum!=1 and sum!=4:
    sum=0
    while temp!=0:
        rem=temp%10
        sum=sum+rem*rem
        temp=temp//10
    temp==sum
if num==1:
    print("HAPPY NUMBER")
else:
    print(num,"NOT HAPPY NUMBER")
