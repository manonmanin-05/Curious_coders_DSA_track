try:
    print("Enter value")
    interger,strings,character=input().split() 
    print(interger,"\n",strings,"\n",character)
except:
    if type(interger) is not int:
        print("Incorrect type.try again!")   
