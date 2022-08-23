password=input("enter the password :  ")
p=len(password)
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chr = "!@#$%^&*()-+"
n=0
l=0
u=0
s=0
i=0
while i<len(password):
    if password[i] in numbers:
        n=n+1
    if password[i] in lower_case:
        l=l+1
    if password[i] in upper_case:
        u=u+1
    if password[i] in special_chr:
        s=s+1
    i=i+1
if p>=6 and n>=1 and l>=1 and u>=1 and s>=1:
    print("strong password")