print("Enter Value")
try:
    val1,val2,val3=map(int,input().split())
    val=val1+val2+val3
    if val == 180:
        print("the triangle can be formed")
    else:
        print("The Triangle cannot be formed")
except:
    print("Incorrect type.try again!")  


