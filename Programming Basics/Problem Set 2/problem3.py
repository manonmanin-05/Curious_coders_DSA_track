try:
    print("write your first name")
    fname=input()
    print("Write your last name")
    lname=input()
    print("How many time you want to print you name?")
    n=int(input())
    if n >0:
        for i in range(n):
            print(fname+" "+lname)
    else:
        print("value must be greater than 0")
except:
    print("Incorrect type.try again!") 
