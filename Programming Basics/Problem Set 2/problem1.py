try:
    print("Enter the X value")
    x=int(input())
    print("Enter the Y value")
    y=int(input())
    if y > 0:          
        for i in range(y):
            print(x)
    else:
        print("the value should be higher than 0")
except:
    print("Incorrect type.try again!")   
