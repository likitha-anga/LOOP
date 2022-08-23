# a
# ab
# abc
# abcd
# abcde

# A
# A B
# A B C
# A B C D
# A B C D E

n=int(input("enter the rows:"))
i=1
while i<=n:
    j=0
    k=ord("A")
    while j<i:
        print(chr(k+j),end=" ")
        j+=1
    print()
    i+=1
    
    
    
    
