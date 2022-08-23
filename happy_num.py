# n=int(input("enter the number:"))
# sum=0
# rem=0
# while n>0:
#     rem=n%10
#     sum=sum+rem*rem
#     n=n//10
# result=0
# while result!=1 and result!=4:
#     if result==1:
#         print(n,"happy number")
#         break
#     else:
#         print(n,"not happy number")
#         break


i=0
while i<10:
    i+=1
    if i==4 or i==9:
        continue
    print(i)
    
    
# i=0
# while i<=10:
    # if i==6:
        # break
    # print(i)
    # i+=1