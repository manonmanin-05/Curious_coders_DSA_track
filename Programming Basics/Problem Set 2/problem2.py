try:
    print("Enter the X value")
    x=int(input())
    if x >0:
        for i in range(x,1001,x):
            print(i)
    else:
        print("value must be greater than 0")
except:
    print("Incorrect type.try again!") 
