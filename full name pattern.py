i=1
while i<=13:
    j=1
    while j<=13:
        if i==1 or i==13 or j==1 or j==13:
            print("l",end=" ")
        elif i==2 or i==12 or j==2 or j==12:
            print("i",end=" ")
        elif i==3 or i==11 or j==3 or j==11:
            print("k",end=" ")
        elif i==4 or i==10 or j==4 or j==10:
            print("i",end=" ")
        elif i==5 or i==9 or j==5 or j==9:
            print("t",end=" ")
        elif i==6 or i==8 or j==6 or j==8:
            print("h",end=" ")
        elif i==j==7:
            print("a",end=" ")
        j+=1
    print()
    i+=1