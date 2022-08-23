num=int(input("enter the number:"))
sum=0
temp=num
while temp>0:
    digit=num%10
    sum=sum+digit**digit
    temp=temp//10
if num==sum:
    print("armstrong number")
else:
    print("not an armstrong number")
    