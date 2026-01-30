print("Enter the size")
try:
    size=int(input())
    match size:        
        case 29:
            print("small")
        case 30:
            print("Medium")
        case 38:            
            print("Large")
        case 42:
            print("XLarge")
        case _:
            print("Incorrect size or Unavailable")       
except:
    print("Incorrect type.try again!")   
