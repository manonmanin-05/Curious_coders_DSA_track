print("Enter the mark")
try:
    mark=int(input())
    if mark in range(101):
        if mark >= 90:
            print("GRADE A")
        elif mark >= 80:
            print("GRADE B")
        elif mark >= 70:
            print("GRADE C")
        elif mark >= 35:
            print("GRADE E")
        else:
            print("FAIL")        
    else:
        print("the number is not in the range")        
except:
    print("Incorrect type.try again!")   
