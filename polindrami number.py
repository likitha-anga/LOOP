n=int(input("enter the number:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10
if n==sum:
    print("polindrami number")
else:
    print("not a polindrami number")

    

    
    
    
